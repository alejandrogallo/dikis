import configparser


_CONFIGURATION = None


def get_configuration():
    if _CONFIGURATION is None:
        _CONFIGURATION = configparser.ConfigParser()
    return _CONFIGURATION
