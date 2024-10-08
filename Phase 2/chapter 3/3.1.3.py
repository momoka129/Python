from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Program Files/Python311/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1,2,3,4,5])

# every data in the list will be 
# def func(data):
#     return data * 10

# rdd2 = rdd.map(func)

# chain call: all return rdd data type
rdd2 = rdd.map(lambda x: x * 10 +5).map(lambda x: x / 3)

print(rdd2.collect())

sc.stop()