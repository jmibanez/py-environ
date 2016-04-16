import mock
from six.moves.configparser import SafeConfigParser

from py_environ import *

def test_to_environ_key():
    assert to_environ_key('Foo') == 'FOO'
    assert to_environ_key('foo') == 'FOO'
    assert to_environ_key('foo.bar') == 'FOO_DOT_BAR'
    assert to_environ_key('foo-bar') == 'FOO_BAR'
    assert to_environ_key('Foo:Bar') == 'FOO_BAR'

@mock.patch.dict(os.environ, {'SECTION1_VAR_ONE': 'foo',
                              'SECTION2_VAR_TWO': 'bar'})
def test_wrapper_get():
    config = EnvironmentConfigWrapper(SafeConfigParser())
    config.add_section('Section1')
    config.add_section('Section2')

    config.set('Section1', 'var_one', 'null')

    config.set('Section2', 'var_two', 'localhost')
    config.set('Section2', 'opt_three', '9092')

    assert config.get('Section1', 'var_one') == 'foo'
    assert config.get('Section2', 'var_two') == 'bar'
    assert config.get('Section2', 'opt_three') == '9092'


@mock.patch.dict(os.environ, {'SECTION1_VAR_ONE': 'foo',
                              'SECTION2_OPT_THREE': '1234',
                              'SECTION3_FLOAT_VAR2': '0.4',
                              'SECTION3_SHOULD_FOO': 'False'})
def test_wrapper_get_type_coercion():
    config = EnvironmentConfigWrapper(SafeConfigParser())
    config.add_section('Section1')
    config.add_section('Section2')
    config.add_section('Section3')
    config.add_section('Section4')

    config.set('Section1', 'var_one', 'null')

    config.set('Section2', 'var_two', 'localhost')
    config.set('Section2', 'opt_three', '9092')
    config.set('Section2', 'opt_four', '42')

    config.set('Section3', 'float_var', '0.2')
    config.set('Section3', 'float_var2', '0.2')
    config.set('Section3', 'should_foo', 'True')
    config.set('Section3', 'should_bar', 'True')

    # Basic tests
    assert config.get('Section1', 'var_one') == 'foo'
    assert config.get('Section2', 'var_two') == 'localhost'
    assert config.getint('Section2', 'opt_three') == 1234
    assert config.getint('Section2', 'opt_four') == 42
    assert config.getfloat('Section3', 'float_var') == 0.2
    assert config.getfloat('Section3', 'float_var2') == 0.4
    assert config.getboolean('Section3', 'should_foo') == False
    assert config.getboolean('Section3', 'should_bar') == True

    # Tests against getboolean coercion
