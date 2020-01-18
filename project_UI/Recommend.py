from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import os

spark = SparkSession.builder \
    .config("spark.sql.shuffle.partitions", 2) \
    .appName("reco") \
    .master("local[2]") \
    .getOrCreate()
jobs = spark.read \
    .option("header", "true") \
    .option("delimiter", ",") \
    .option("inferSchema", 'true') \
    .csv("/home/sunbeam/ml/project_UI/final_clean_csv.csv")

jobs.createGlobalTempView("Naukri")
def recommend(industry_f,location_f,skills_f,avg_experience_f):

    industry=industry_f
    location=location_f
    skills=skills_f
    avg_exp= str(avg_experience_f)
    print("hello World")

    result=spark.newSession(). \
        sql("select company,jobtitle,count(numberofpositions) as Openings from global_temp.Naukri "
            "where industry='"+industry+
            "' AND joblocation_address='"+location+
            "' AND skills='"+skills+
            "' group by company,jobtitle order by Openings desc").collect()
    #
    # result.repartition(1).write \
    #         .format("com.databricks.spark.csv") \
    #         .option("header", "true") \
    #         .json("./static/abc.json", mode='overwrite')

    # result.show(truncate=False)
    # first_res=result.first()
    return result

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=

#
#     #demo:
# def recommend():
#     spark = SparkSession.builder \
#         .config("spark.sql.shuffle.partitions", 2) \
#         .appName("reco") \
#         .master("local[2]") \
#         .getOrCreate()
#     jobs = spark.read \
#         .option("header", "true") \
#         .option("delimiter", ",") \
#         .option("inferSchema", 'true') \
#         .csv("/home/sunbeam/ml/project_UI/final_clean_csv.csv")
#
#     # jobs.write.parquet("final_clean_csv.parquet")
#     # parquetFile = spark.read.parquet("final_clean_csv.parquet")
#     #
#     # # Parquet files can also be used to create a temporary view and then used in SQL statements.
#     # parquetFile.createOrReplaceTempView("Naukri")
#
#     jobs.createGlobalTempView("Naukri")
#
#     result=spark. \
#         sql("select company,jobtitle,count(numberofpositions) as Openings from global_temp.Naukri "
#             "where industry='IT-Software / Software Services' "
#             "AND joblocation_address='Bengaluru' "
#             "AND skills='ITES' "
#             "OR avg_experienvce=1 "
#             "group by company,jobtitle "
#             "order by Openings desc")
#         # .write.saveAsTable("JobsAndCompany")
#     # result.write.csv("./JobsAndCompany")
#     result.write \
#             .format("com.databricks.spark.csv")\
#             .option("header", "true")\
#             .csv("/home/sunbeam/ml/project_UI/static1/abc",mode='overwrite')
#     result.show(truncate=False)
#     # os.rename('/home/sunbeam/ml/project_UI/static1/abc/*.csv','/home/sunbeam/ml/project_UI/static1/abc/abc.csv')
#     spark.stop()
#
# recommend()