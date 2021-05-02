import requests
import urllib

# from gensim.models import Word2Vec
from gensim.models import FastText

from scrayping import get_page_content
from text_embedding import divid_word


books_list = requests.get(
    'http://pubserver2.herokuapp.com/api/v0.1/books').json()
text_list = []
for book in books_list:
    book_id = book["book_id"]
    try:
        res = urllib.request.urlopen(
            'http://pubserver2.herokuapp.com/api/v0.1/books/{}/content?format=html'.format(book_id))
        text_list += get_page_content(res)
    except urllib.error.HTTPError:
        pass

sentences = []
for text in text_list:
    sentences.append(divid_word(text))


# model = Word2Vec(sentences=sentences, vector_size=100,
#                  window=5, min_count=1, workers=4)

# model = FastText(vector_size=4, window=3, min_count=1)
# model.build_vocab(sentences=sentences)
# model.train(sentences=sentences, total_examples=len(sentences), epochs=10)
model = FastText(vector_size=4, window=3, min_count=1,
                 sentences=sentences, epochs=10)
vec = model.wv['computer']
print(vec)

model.save("../train_model/word2vec.model")
