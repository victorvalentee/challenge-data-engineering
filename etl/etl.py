import os
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import when
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# Go to the ETL root directory
os.chdir("/opt/airflow/etl")


# Create SparkSession as a global 
# so I don't have to inject it as a dependency
spark = SparkSession.builder.appName("MT-DE-Exercise").getOrCreate()


def extract(input_path: str) -> pyspark.sql.DataFrame:
    """Read the CSV file into a DataFrame"""

    raw_df = spark.read.csv(input_path, header=True, inferSchema=True)
    return raw_df


def transform(df: pyspark.sql.DataFrame) -> pyspark.sql.DataFrame:
    """Create new categorical columns based on project requirements"""

    # Create new cat column based on housing_median_age values
    df = df.withColumn("hma_cat", 
        when(df.housing_median_age < 18, "de_0_ate_18")
        .when((df.housing_median_age >= 18) & (df.housing_median_age < 29), "ate_29")
        .when((df.housing_median_age >= 29) & (df.housing_median_age < 37), "ate_37")
        .otherwise("acima_37")
    )

    # Create new cat column based on longitude values
    df = df.withColumn("c_ns", when(df.longitude < -119, "norte").otherwise("sul"))

    # Rename newly created columns
    df = df.withColumnRenamed("hma_cat", "age").withColumnRenamed("c_ns", "california_region")

    return df


def save_parquet(df: pyspark.sql.DataFrame, output_path: str) -> None:
    """Save DataFrame as parquet file"""

    # Define parquet schema based on project requirements
    write_schema = StructType([
        StructField("age", StringType()),
        StructField("california_region", StringType()),
        StructField("total_rooms", DoubleType()),
        StructField("total_bedrooms", DoubleType()),
        StructField("population", DoubleType()),
        StructField("households", DoubleType()),
        StructField("median_house_value", DoubleType())
    ])

    df.write.option("schema", write_schema).mode("overwrite").parquet(output_path)


if __name__ == "__main__":
    # Extract
    raw_df = extract("./input/california_housing_train.csv")
    
    # Transform
    transformed_df = transform(raw_df)
    
    # Load
    save_parquet(transformed_df, "./output/categorical")

