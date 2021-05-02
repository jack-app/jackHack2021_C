import numpy as np


def get_cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def embedrank(text_vec, word_vec_dict, rank=3):
    cos_sims = {}
    for word, word_vec in word_vec_dict.items():
        cos_sim = get_cos_sim(word_vec, text_vec)
        cos_sims[word] = cos_sim

    cos_sims_sorted = sorted(
        cos_sims.items(), key=lambda x: x[1], reverse=True)

    return cos_sims_sorted[:rank]
