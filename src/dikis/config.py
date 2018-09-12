import configparser


_CONFIGURATION = None


def get_configuration():
    global _CONFIGURATION
    if _CONFIGURATION is None:
        _CONFIGURATION = configparser.ConfigParser()
    return _CONFIGURATION
