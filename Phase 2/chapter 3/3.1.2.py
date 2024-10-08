from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# load python object into Spark - RDD object
rdd1 = sc.parallelize([1,2,3,4,5])
rdd2 = sc.parallelize((1,2,3,4,5))
rdd3 = sc.parallelize("Good morning...")
rdd4 = sc.parallelize({1,2,3,4,5})
rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})

rdd = sc.textFile("Phase 2/chapter 3/readFile_rdd.txt")

print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

print(rdd.collect())

sc.stop()
   