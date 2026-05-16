from pyspark import SparkContext
sc = SparkContext()
counts = (sc.textFile("data.txt")
            .flatMap(lambda line: line.split())
            .map(lambda word: (word, 1))
            .reduceByKey(lambda a, b: a + b))