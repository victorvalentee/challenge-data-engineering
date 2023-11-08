import os
import pyspark
import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# Go to the ETL root directory
os.chdir("/opt/airflow/etl")


# Create SparkSession as a global 
# so I don't have to inject it as a dependency
spark = SparkSession.builder.appName("MT-DE-Exercise").getOrCreate()


def extract(input_path: str) -> pyspark.sql.DataFrame:
    """Read the Parquet file into a DataFrame"""
    
    raw_df = spark.read.parquet(input_path)
    return raw_df


def transform(df: pyspark.sql.DataFrame) -> pyspark.sql.DataFrame:
    """Create new agg columns based on project requirements"""

    # Aggregate dataframe on `age` and `california_region`
    # Get the sum of the population 
    # and the mean of the median_house_value

    df_transformed = df.groupBy("age", "california_region").agg(
            F.sum('population').alias('s_population'),
            F.avg('median_house_value').alias('m_median_house_value')
    )

    # Sort dataframe (descending) based on `m_median_house_value` column
    df_sorted = df_transformed.orderBy(col("m_median_house_value").desc())

    return df_sorted


def save_parquet(df: pyspark.sql.DataFrame, output_path: str) -> None:
    """Save DataFrame as parquet file"""

    # Define parquet schema based on project requirements
    write_schema = StructType([
        StructField("age", StringType()),
        StructField("california_region", StringType()),
        StructField("s_population", DoubleType()),
        StructField("m_median_house_value", DoubleType())
    ])

    df.write.option("schema", write_schema).mode("overwrite").parquet(output_path)


def main():
    # Extract
    raw_df = extract("./output/categorical")
    
    # Transform
    transformed_df = transform(raw_df)
    
    # Load
    save_parquet(transformed_df, "./output/final")


if __name__ == "__main__":
    main()

