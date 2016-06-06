import logging
import os

from six.moves.configparser import SafeConfigParser

log = logging.getLogger(__name__)


TRUE_EQUIVALENT_STRINGS = ["1", "yes", "true", "on"]
FALSE_EQUIVALENT_STRINGS = ["0", "no", "false", "off"]

def to_environ_key(k):
    return k.upper() \
            .replace('-', '_') \
            .replace('.', '_DOT_') \
            .replace(' ', '_') \
            .replace(':', '_') \


class EnvironmentConfigWrapper(SafeConfigParser, object):
    def has_option(self, section, option):
        env_prefix = to_environ_key(section)
        env_option = to_environ_key(option)
        env_name = "%s_%s" % (env_prefix, env_option)

        if env_name in os.environ:
            return True
        else:
            return super(EnvironmentConfigWrapper, self).has_option(section, option)

    def get(self, section, option):
        env_prefix = to_environ_key(section)
        env_option = to_environ_key(option)
        env_name = "%s_%s" % (env_prefix, env_option)

        if env_name in os.environ:
            return os.environ[env_name]
        else:
            return super(EnvironmentConfigWrapper, self).get(section, option)
        
