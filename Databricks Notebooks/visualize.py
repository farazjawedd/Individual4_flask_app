# Databricks notebook source
# Databricks notebook source
# Imnporting required packages and libraries
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession
from pyspark.sql.utils import AnalysisException
import pandas as pd



# COMMAND ----------

def validate_and_plot_data(result):
    # Validate result
    if result.rdd.isEmpty():
        raise ValueError("Query returned no results")

    # Convert the Spark DataFrame to a Pandas DataFrame
    result_pd = result.toPandas()

    # Plot the relationship between Hp and Price by Make
    result_pd.plot(x='continent', y=['avg_freedom', 'avg_corruption'], kind='bar')
    plt.title("Continents freedom vs corruption")
    plt.xlabel("Continent")
    plt.ylabel("Freedom & Corruption")
    plt.savefig("../plot.png")
    plt.show()


# COMMAND ----------

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()
try:
    result = spark.sql(
        """
        SELECT *
        FROM happiness_final
        """
    )
    validate_and_plot_data(result)
except AnalysisException as e:
    print(f"SQL query error: {e}")
except ValueError as e:
    print(f"Data validation error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
