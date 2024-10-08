from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Program Files/Python311/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(["Good luck", "To EVery one"])

rdd2 = rdd.map(lambda x: x.split(" "))
print(rdd2.collect())   # output: [['Good', 'luck'], ['To', 'EVery', 'one']]

# un-nesting
rdd3 = rdd.flatMap(lambda x: x.split(" "))
print(rdd3.collect())