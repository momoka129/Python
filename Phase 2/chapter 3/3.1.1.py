# Apache Spark 是用于大规模数据（large-scale data)处理的统一（unified)分析引擎

from pyspark import SparkConf, SparkContext

# create SparkConf class object
cf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# create SparkContext object based on SparkConf class object or get existing one
sc = SparkContext.getOrCreate(conf=cf)

# print the version of spark
print(sc.version)

# stop the sparkContext object from running
sc.stop()
