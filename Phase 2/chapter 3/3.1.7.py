# rdd.filter(func)
# retains the data -- which return true to the statement 
# func: T -> bool

from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Program Files/Python311/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1,2,3,4,5])

# reserve odd
rdd_odd = rdd.map(lambda x: x % 2 != 0)
rdd_odd_2 = rdd.filter(lambda num: num % 2 != 0)
print(rdd_odd.collect())
print(rdd_odd_2.collect())