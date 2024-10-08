from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Program Files/Python311/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.textFile("Phase 2/chapter 3/316.text")

# extract all the words
rdd_words = rdd.flatMap(lambda x: x.split(" "))

# set all word into a two-tuple: key-word, value-1
TwoTuple_rdd = rdd_words.map(lambda word: (word, 1))
print(TwoTuple_rdd.collect())

# grouping and summation
count_word_rdd = TwoTuple_rdd.reduceByKey(lambda a, b: a + b)
print(count_word_rdd.collect())