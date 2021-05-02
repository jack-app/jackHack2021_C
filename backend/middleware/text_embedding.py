from janome.tokenizer import Tokenizer
from gensim.models.doc2vec import Doc2Vec
from gensim.models import FastText

doc2vec_model_path = 'train_model/doc2vec.model'
fasttext_model_path = 'train_model/fasttext.model'
t = Tokenizer()


def text_embedding(text):
    word_list = list(t.tokenize(text, wakati=True))
    for token in t.tokenize(text):
        print(token)

    model = Doc2Vec.load(doc2vec_model_path)
    vec = model.infer_vector(word_list)

    return vec


def words_embedding(text):
    word_list = list(t.tokenize(text, wakati=True))

    model = FastText.load(fasttext_model_path)
    vecs = {}
    for word in word_list:
        vec = model.wv[word]
        vecs[word] = vec.tolist()

    return vecs
