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
