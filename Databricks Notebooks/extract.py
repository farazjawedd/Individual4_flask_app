# Databricks notebook source
from pyspark.sql import SparkSession
from delta.tables import DeltaTable
import pandas as pd

# COMMAND ----------

#load the data into a pandas dataframe
data = pd.read_csv(
        "https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv"
    )

# COMMAND ----------

#do some column cleaning as otherwise it wont be stored in the delta lake
data.columns = data.columns.str.replace(":", "")
data.columns = data.columns.str.replace("+", "")
data.columns = data.columns.str.replace(" ", "_")


# COMMAND ----------

data

# COMMAND ----------

#convert pandas dataframe to spark dataframe
spark = SparkSession.builder.getOrCreate()
spark_df = spark.createDataFrame(data)

# COMMAND ----------

# Write the DataFrame to a Delta Lake table (if the table already exists, overwrite it)
spark_df.write.format("delta").mode("overwrite").saveAsTable('happiness')
