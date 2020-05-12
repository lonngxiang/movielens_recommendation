import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
from conf.redis_connect import *
import numpy as np


def combine(x):
    return x['title'] + " " + x['movietype']


def movies_combin(movies):
    """Combined movie tpye data"""
    movies['Combined_Data'] = movies.apply(lambda x: combine(x), axis=1)
    return movies


def rec_content(movies, cosine_sim_tf):
    movie_ids = movies['title'].tolist()
    for i in movie_ids:
        movie_index = movies[movies.title == i].index.values[0]
        movie_id = movies[movies.title == i]["item_id"].values[0]
        movie_id = int(movie_id)  # numpy.int --> python int
        similar_movies = list(enumerate(cosine_sim_tf[movie_index]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]
        # sorted_similar_movies
        contents_list = []
        for j in range(10):
            contents_list.append((movies['title'][movies.index == (sorted_similar_movies[j][0])]).values[0])
        # print(contents_list)
        save_content(i, movie_id, contents_list)


def content_rank(movies):
    movies = movies_combin(movies)
    """using TFIDF"""
    # tf = TfidfVectorizer()
    # count_matrix = tf.fit_transform(movies["Combined_Data"])
    """Using Count Vectorizer"""
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(movies["Combined_Data"])
    cosine_sim_tf = cosine_similarity(count_matrix)
    # 存储
    np.save(file="./../data/data11.npy", arr=cosine_sim_tf)
    rec_content(movies, cosine_sim_tf)
