import re
import os
import json
import dikis.dicts
from milon.dictionaries import DictionaryHeEn
from milon.transliteration import ascii_to_unicode


class Dictionary(dikis.dicts.Dictionary):

    def __init__(self):
        dikis.dicts.Dictionary.__init__(self, 'milon En - He')
        self.milon = DictionaryHeEn()

    def lookup(self, word):
        return self.milon.lookup_ascii(word)

    def prompt_formater(self, word):
        return ascii_to_unicode(word)

    def header_formater(self, word):
        return """\
{w[translated]}
{w[translation][0]} ({w[part_of_speech]})
{w[inflections]}
{w[samples]}
""".format(w=word)
