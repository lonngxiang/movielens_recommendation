import pandas as pd


def read_ratings():
    """load user item rating data"""
    column_names = ['user_id', 'item_id', 'rating', 'timestamp']
    links = pd.read_csv('./data/ratings.dat', sep="::", names=column_names)
    return links


def read_movies():
    """load movie profile data"""
    column_names1 = ['item_id', 'title', 'movietype']
    movies = pd.read_csv('./data/movies.dat', sep="::", names=column_names1)
    return movies