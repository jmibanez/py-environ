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


class EnvironmentConfigWrapper(object):
    def __init__(self, config_parser):
        if config_parser is None:
            raise ValueError("Must pass a ConfigParser to wrap")

        self.config_parser = config_parser

    def defaults(self):
        return self.config_parser.defaults()

    def sections(self):
        return self.config_parser.sections()

    def add_section(self, section):
        return self.config_parser.add_section(section)

    def set(self, section, option, value):
        return self.config_parser.set(section, option, value)

    def remove_option(self, section, option):
        return self.config_parser.remove_option(section, option)

    def has_option(self, section, option):
        env_prefix = to_environ_key(section)
        env_option = to_environ_key(option)
        env_name = "%s_%s" % (env_prefix, env_option)

        if env_name in os.environ:
            return True
        else:
            return self.config_parser.has_option(section, option)

    def get(self, section, option):
        env_prefix = to_environ_key(section)
        env_option = to_environ_key(option)
        env_name = "%s_%s" % (env_prefix, env_option)

        if env_name in os.environ:
            return os.environ[env_name]
        else:
            return self.config_parser.get(section, option)

    def getint(self, section, option):
        v = self.get(section, option)
        log.debug("get (to int): %s, %s => %s", section, option, v)
        return int(v)

    def getfloat(self, section, option):
        v = self.get(section, option)
        log.debug("get (to float): %s, %s => %s", section, option, v)
        return float(v)

    def getboolean(self, section, option):
        v = self.get(section, option)
        log.debug("get (to bool): %s, %s => %s", section, option, v)

        if v.lower() in TRUE_EQUIVALENT_STRINGS:
            return True
        elif v.lower() in FALSE_EQUIVALENT_STRINGS:
            return False
        else:
            raise ValueError(v)
        
