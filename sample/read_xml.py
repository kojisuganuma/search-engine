# -*- coding: utf-8 -*-

from __future__ import print_function # Python 2/3 compatibility
from pyspark.sql import SQLContext
from pyspark import SparkConf, SparkContext
from pyspark.sql.types import *

### test code: read_xml ###
# command $ spark-submit --packages com.databricks:spark-xml_2.10:0.4.1 --master local read_xml.py 2> /dev/null
if __name__ == '__main__':
	sc = SparkContext("local", "Test Read XML")
	sqlContext = SQLContext(sc)

	df = (sqlContext.read
			.format('com.databricks.spark.xml')
			.options(rowTag='doc')
			.load('wiki_00.xml'))
			# .load('books.xml'))
			# .load('../data/full/raw/extracted/AA/wiki_00.xml'))

	print(df.printSchema())
	print(type(df))

	# (df.select("author", "_id").write
	# 	.format('com.databricks.spark.xml')
	# 	.options(rowTag='book', rootTag='books')
	# 	.save('newbooks.xml'))