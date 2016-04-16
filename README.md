py-environ: ConfigParser with environmental override
====================================================

This is a ConfigParser wrapper that uses an underlying ConfigParser to
load and parse configuration with the ability to override option
values from the environment.


Usage
=====
```
    from py_environ import EnvironmentConfigWrapper

    # Create a wrapper around a config parser
    config = EnvironmentConfigWrapper(SafeConfigParser())
    
    # Use as is
    option_one_str = config.get('My Section', 'option_one')
    option_two_int = config.getint('My Section', 'option_two)
    
    # In this case, the option value in the ConfigParser is overridden
    # by the environment variable MY_SECTION_OPTION_THREE
    option_three = config.get('My Section', 'option_three')
```

