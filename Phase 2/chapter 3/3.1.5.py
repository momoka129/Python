# rdd.reduceByKey(func)
# auto group by key
# func only handle with data manipulation, not grouping
# func: (v,v) -> v
# 2 parameters, return 1 value, all same data type
# two-tuple: first is the key 

from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Program Files/Python311/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([('male', 9), ('male', 10), ('female', 9.5), ('female', 10), ('male', 10)])

rdd2 = rdd.reduceByKey(lambda a, b: a + b) 
print(rdd2.collect())

sc.stop()
