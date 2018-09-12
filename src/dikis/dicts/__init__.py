

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


class Dictionary:

    def __init__(self, name):
        self.name = name

    def lookup(word):
        raise NotImplementedError

    def header_formater(word):
        raise NotImplementedError

    def prompt_formater(word):
        raise NotImplementedError
