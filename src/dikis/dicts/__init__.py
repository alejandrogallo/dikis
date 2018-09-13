import re
import os
import glob


_CURRENT_DICT = None


def get_dict():
    global _CURRENT_DICT
    return _CURRENT_DICT


def get_dict_from_name(dict_name):
    """
    Get a dictionary instance from name
    :param dict_name: Name of a dictionary
    :type  dict_name: str
    """
    mod = __import__(
        'dikis.dicts.' + dict_name,
        globals(),
        locals(),
        ['Dictionary'],
        0
    )
    return mod.Dictionary()


def set_dict(dictionary):
    global _CURRENT_DICT
    _CURRENT_DICT = dictionary


def set_dict_from_name(dict_name):
    dic = get_dict_from_name(dict_name)
    set_dict(dic)


def list_dictionary_names():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    names = []
    for n in os.listdir(current_dir):
        if not re.match(r"^_.*", n):
            names.append(n.replace('.py', ''))
    return names


class Dictionary:

    def __init__(self, name):
        self.name = name

    def lookup(self, word):
        raise NotImplementedError

    def header_formater(self, word):
        raise NotImplementedError

    def prompt_formater(self, word):
        raise NotImplementedError
