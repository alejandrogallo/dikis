import dikis.config
import configparser


def test_config():
    c = dikis.config.get_configuration()
    assert(isinstance(c, configparser.ConfigParser))
