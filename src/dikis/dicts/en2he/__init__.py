import re
import os
import json
import dikis.dicts


data_file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'dict-en-he.json'
)

assert(os.path.exists(data_file))


class Dictionary(dikis.dicts.Dictionary):

    def __init__(self):
        dikis.dicts.Dictionary.__init__(self, 'aramorph')
        self.limit = 20
        with open(data_file) as fd:
            self.words = json.load(fd)

    def lookup(self, word):
        results = []
        for w in self.words:
            if re.match(word, w.get('translated')):
                results.append(w)
            if len(results) > self.limit:
                return results
        return results

    def header_formater(self, word):
        return """\
{w[translated]}
{w[translation][0]} ({w[part_of_speech]})
{w[inflections]}
{w[samples]}
""".format(w=word)

