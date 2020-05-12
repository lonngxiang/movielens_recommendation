from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.recommendation import ALSModel
from pyspark.sql import Row
from conf.redis_connect import *

import pandas as pd
import os
os.environ["PYSPARK_PYTHON"] = "/Users/lonng/opt/anaconda3/python.app/Contents/MacOS/python"


def spark_seesion():
    spark = SparkSession \
        .builder \
        .appName("ALSExample") \
        .getOrCreate()
    return spark


def als_model(training):
    als = ALS(maxIter=5, regParam=0.01, userCol="user_id", itemCol="item_id", ratingCol="rating",
              coldStartStrategy="drop")
    model = als.fit(training)
    model.save("./../data/als_model11")
    return model


def cf_rank(links, movies):
    spark = spark_seesion()
    ratings = spark.createDataFrame(links.iloc[:100000,:])
    (training, test) = ratings.randomSplit([0.9, 0.1])
    model = als_model(training)
    userRecs = model.recommendForAllUsers(10).collect()

    for i in userRecs:
        user = i.user_id
        # print(i.recommendations)
        cf_list = []
        for j in i.recommendations:
            item = j.item_id
            # print(j.rating)
            item = movies[movies.item_id == item]["title"].values[0]
            cf_list.append(item)
        save_cf(user, cf_list)

