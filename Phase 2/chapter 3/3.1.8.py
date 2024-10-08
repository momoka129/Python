# rdd.distinct()
# deduplication
# no parameter

from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Program Files/Python311/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.textFile("Phase 2/chapter 3/316.text")

# extract all the words
rdd_words = rdd.flatMap(lambda x: x.split(" "))
print(rdd_words.collect())

# deduplication
rdd_single = rdd_words.distinct()
print(rdd_single.collect())