# python objects / file -- input
# rdd -- compute
# python / file -- output

# collect: RDD->list

# rdd.reduce(func):
# func:(T,T) -> T

# take:
# take out the first n elements 

# count:
# how many elements in the rdd

from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Program Files/Python311/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(range(1,10))   # 1~9

# collect:
rdd_list:list = rdd.collect()
print(rdd_list)
print(type(rdd_list)) # list

# reduce:
num = rdd.reduce(lambda a, b: a + b)
print(num)
print(type(num)) # int

# take:
take_list = rdd.take(3)
print(take_list)
print(type(take_list)) # list

# count
num_count = rdd.count()
print(f"rdd have {num_count} elements")

sc.stop()