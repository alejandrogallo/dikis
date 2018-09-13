from dikis.dicts import *


def test_set_dict_from_name():
    a = set_dict_from_name('aramorph')
    assert(a is None)
    d = get_dict()
    assert(d is not None)


def test_get_dict_from_name():
    d = get_dict_from_name('aramorph')
    assert(d is not None)


def test_base_dict():
    d = Dictionary('test')

    assert(d.name == 'test')

    try:
        d.lookup('hi')
    except NotImplementedError:
        assert(True)
    else:
        assert(False)

    try:
        d.header_formater('hi')
    except NotImplementedError:
        assert(True)
    else:
        assert(False)

    try:
        d.prompt_formater('hi')
    except NotImplementedError:
        assert(True)
    else:
        assert(False)


def test_list():
    names = list_dictionary_names()
    assert(names)
    assert('__init__.py' not in names)
    assert('__init__' not in names)
    assert('aramorph' in names)
    assert('en2he' in names)
