import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
import requests
import json

conf = SparkConf()
conf.set("spark.pyspark.python", "python")  # Use "python" instead of "python3"
sc = SparkContext(conf=conf)


spark = SparkSession.builder \
    .master("local[*]") \
    .appName("MyApp") \
    .getOrCreate()
