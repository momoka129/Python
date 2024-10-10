from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Program Files/Python311/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

file_rdd = sc.textFile(".......................")

# TODO require 1: Top 3 time periods for popular searches (hourly precision)
# 1.1 take out all time and convert into hours
# 1.2 convert to (hour, 1) tuple
# 1.3 group by key and aggregate values
# 1.4 sort by descending order
# 1.5 take the top three
result_1 = file_rdd.map(lambda x: (x.split("\t")[0][:2], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
    take(3)
print(result_1)


