

def main(spark, path):
    df_list = [('EUR', 4.71),
               ('USD', 4.35),
               ('GBP', 5.37),
               ('INR', 0.05),
               ('CHF', 4.73)
    ]
 
    # budujemy data frame w Sparku
    df = spark.createDataFrame(df_list,
                            # nazwy kolumn:
                            ["curr", "value"])
    
    df.write.format("csv").mode("overwrite").save(path)



