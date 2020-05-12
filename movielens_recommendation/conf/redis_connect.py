import redis
import numpy as np
import json


def save_hot(data):
    rs = redis.StrictRedis(host='127.0.0.1', db=5)
    rs.hset('hot_rec', 'hot_list', json.dumps({"hot": data}))
    print("save hot list recommend")


def read_hot():
    rs = redis.StrictRedis(host='127.0.0.1', db=5)
    data = json.loads(rs.hget('hot_rec', 'hot_list'))['hot']
    return data


def save_content(name, movie_id, data):
    rs = redis.StrictRedis(host='127.0.0.1', db=5)
    rs.hset('content_rec', movie_id, json.dumps({name: data}))
    print("save content list recommend")


def read_content(movie_id):
    rs = redis.StrictRedis(host='127.0.0.1', db=5)
    data = json.loads(rs.hget('content_rec', movie_id))
    return data


def save_cf(user,cf_list):
    rs = redis.StrictRedis(host='127.0.0.1', db=5)
    rs.hset('cf_rec', user, json.dumps({"content": cf_list}))
    print("save cf list recommend")


def read_cf(user_id):
    rs = redis.StrictRedis(host='127.0.0.1', db=5)
    data = json.loads(rs.hget('cf_rec', user_id))
    return data