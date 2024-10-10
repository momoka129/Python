# saveAsTextFile
# rdd -> folder: text file

# need Hadoop ...
# heima 151

from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Program Files/Python311/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(range(1,6)) 

rdd.saveAsTextFile("Phase 2/chapter 3/3113.text")

sc.stop()