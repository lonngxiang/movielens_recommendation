import pandas as pd
from conf.redis_connect import *


def user_item_merge(links, movies):
    df = pd.merge(links, movies, on="item_id")
    df = df.drop(columns=['timestamp'])
    return df


def hot_rank(links, movies):
    df = user_item_merge(links, movies)
    # top 20 movies based on ratings
    top = df.groupby(['title'])['rating'].mean().sort_values(ascending=False)[:20]
    save_hot(top.index.tolist())



