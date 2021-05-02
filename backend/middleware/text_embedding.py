from janome.tokenizer import Tokenizer
from gensim.models.doc2vec import Doc2Vec

model_path = 'train_model/doc2vec.model'
t = Tokenizer()


def text_embedding(text):
    word_list = list(t.tokenize(text, wakati=True))

    model = Doc2Vec.load(model_path)

    vec = model.infer_vector(word_list)

    return vec


def words_embedding(words):
    pass
