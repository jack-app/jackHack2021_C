import requests
import urllib

from gensim.models.doc2vec import Doc2Vec, TaggedDocument

from scrayping import get_page_content
from text_embedding import divid_word


# URL = 'https://www.aozora.gr.jp/cards/000074/files/427_19793.html'
# text_list = get_page_content(URL)

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

documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(sentences)]
# print(documents)
model = Doc2Vec(documents, vector_size=5, window=2, min_count=1, workers=4)
model.save("../train_model/doc2vec.model")

m = Doc2Vec.load('../train_model/doc2vec.model')

# 分散表現抽出
# vec = model.infer_vector(['檸檬', 'トロッコ', '先生', 'そうか'])
# print(vec)
