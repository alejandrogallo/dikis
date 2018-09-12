import dikis.dicts

import aramorph
import aramorph.transliterate
import aramorph.analyser


class Dictionary(dikis.dicts.Dictionary):

    def __init__(self):
        dikis.dicts.Dictionary.__init__(self, 'aramorph')
        self.analyser = aramorph.analyser.get_analyser()

    def lookup(self, word):
        return self.analyser.analyse(word)

    def prompt_formater(self, word):
        return aramorph.transliterate.b2u(word)

    def header_formater(self, word):
        # {'word': 'سل', 'vowelled': 'سَلَّ', 'root': 'سل', 'pos': 'Perfect verb',
                # 'transliteration': 'salla', 'gloss': 'withdraw + he/it <verb>'}
        return """\
{w[word]} {w[vowelled]} /{w[transliteration]}/
        <{w[pos]}> Root: {w[root]}
    {w[gloss]}
""".format(w=word)
