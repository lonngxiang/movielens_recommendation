"""
autor: loong
data: 202005**
"""
from cleaning.data_cleaning import *
from algorithm.hot_rec import *
from algorithm.content_rec import *
from algorithm.cf_rec import *
from conf.redis_connect import *
from flask import Flask,render_template,request,jsonify,Response

app = Flask(__name__)


def run_hot(links, movies):
    hot_rank(links, movies)


def run_content(movies):
    content_rank(movies)


def run_cf(links, movies):
    cf_rank(links, movies)


def main(links, movies):
    run_hot(links, movies)
    run_content(movies)
    run_cf(links, movies)


@app.route('/test', methods=['GET', 'POST'])
def test():
    hot_rec_list = read_hot()
    print(hot_rec_list)
    content_rec_list = read_content(2)  # item_id 2
    print(content_rec_list)
    for i, j in content_rec_list.items():
        print(i, j)
    # print(movies[movies.item_id == 2]["title"].values[0], content_rec_list)
    cf_rec_list = read_cf(2)  # user_id 2
    print(cf_rec_list)
    return jsonify({'hot': hot_rec_list,"cb": content_rec_list,"cf": cf_rec_list})


if __name__ == '__main__':
    links = read_ratings()
    movies = read_movies()
    main(links, movies)
    app.run(host="0.0.0.0", port=5010)



