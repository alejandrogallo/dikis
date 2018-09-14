import os
import dikis.dicts
try:
    import slob
except ImportError:
    raise ImportError(
        "You don't have slob installed in your system \n"
        "Install it via:\n"
        "\tpip install git+https://github.com/alejandrogallo/slob.git"
    )


class Dictionary(dikis.dicts.Dictionary):

    def __init__(self, slobfile_path, fmt=None, limit=20):
        dikis.dicts.Dictionary.__init__(self, slobfile_path)
        self.limit = limit
        self.fmt = fmt or '{w.content}'
        self.slobfile_path = os.path.expanduser(slobfile_path)
        self.slob = slob.open(self.slobfile_path)

    def lookup(self, word):
        results = []
        done = False
        generator = self.slob.as_dict()[word]
        while not done:
            if len(results) >= self.limit:
                return results
            else:
                try:
                    w = next(generator)
                except StopIteration:
                    return results
                else:
                    results.append(w)

    def header_formater(self, word):
        return self.fmt.format(w=word)
