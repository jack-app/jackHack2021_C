from janome.tokenizer import Tokenizer

t = Tokenizer()


def divid_word(s):
    return list(t.tokenize(s, wakati=True))
