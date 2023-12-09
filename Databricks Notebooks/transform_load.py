# Databricks notebook source
# Databricks notebook source
# Import Required Packages and Libraries
from pyspark.sql import SparkSession
from pyspark.sql.utils import AnalysisException



# COMMAND ----------

# Creating SparkSession
spark = SparkSession.builder.getOrCreate()


def validate_and_execute_query():
    try:
        # Use Spark SQL for transformations
        result = spark.sql(
            """
            SELECT 
                Regional_indicator as continent, 
                AVG(Freedom_to_make_life_choices) as avg_freedom, 
                AVG(Perceptions_of_corruption	) as avg_corruption
            FROM happiness
            GROUP BY Regional_indicator
        """
        )

        # Validate result
        if result.rdd.isEmpty():
            raise ValueError("Query returned no results")

        # Write the result to a Delta table
        result.write.format("delta").mode("overwrite").saveAsTable("happiness_final")

        # Show the result
        result.show()

    except AnalysisException as e:
        print(f"SQL query error: {e}")
    except ValueError as e:
        print(f"Data validation error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# COMMAND ----------

# Run the function
validate_and_execute_query()

# COMMAND ----------


