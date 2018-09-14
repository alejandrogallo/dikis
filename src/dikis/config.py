import os
import configparser


_CONFIGURATION = None


def get_configuration():
    global _CONFIGURATION
    if _CONFIGURATION is None:
        _CONFIGURATION = configparser.ConfigParser()
        _CONFIGURATION.read(os.path.expanduser('~/.config/dikis/config'))
    return _CONFIGURATION
