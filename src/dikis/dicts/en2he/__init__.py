import re
import os
import json
import dikis.dicts
from milon.dictionaries import DictionaryEnHe


class Dictionary(dikis.dicts.Dictionary):

    def __init__(self):
        dikis.dicts.Dictionary.__init__(self, 'milon En - He')
        self.milon = DictionaryEnHe()

    def lookup(self, word):
        return self.milon.lookup(word)

    def header_formater(self, word):
        return """\
{w[translated]}
{w[translation][0]} ({w[part_of_speech]})
{w[inflections]}
{w[samples]}
""".format(w=word)

