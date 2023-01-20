from datetime import datetime
from pyspark.sql.functions import *

def generate_date(spark, read_path, write_path):

    existing_records = spark.read.options(header='True').csv(read_path)

    existing_records.withColumn("datestamp", lit(datetime.now()))

    existing_records.df.write.format("txt").save(write_path)

    

