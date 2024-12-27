import pandas as pd
import requests
import psycopg2
from sqlalchemy import create_engine

# configure sources and destinations

API_URL = .
CSV_SOURCE_PATH = "source_data.csv"
DATABASE_URL = .

# extract data from api

def extract_from_api():
    try:
        print("extracting data from api...")
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        print("data extracted successfully from api.")
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"error extracting data from api: {e}")
        return pd.DataFrame()

# extract data from csv

def extract_from_csv():
    try:
        print(f"extracting data from {CSV_SOURCE_PATH}...")
        return pd.read_csv(CSV_SOURCE_PATH)
    except FileNotFoundError:
        print(f"error: file {CSV_SOURCE_PATH} not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"unexpected error extracting data from csv: {e}")
        return pd.DataFrame()

# transform data

def transform_data(df):
    try:
        print("transforming data...")
        
        # standardize column names
        
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        # example transformations (customize as needed)
        
        if "price" in df.columns and "quantity" in df.columns:
            df["total_value"] = df["price"] * df["quantity"]

        if "timestamp" in df.columns:
            df["timestamp"] = pd.to_datetime(df["timestamp"])

        print("data transformation complete.")
        return df
    except Exception as e:
        print(f"error transforming data: {e}")
        return pd.DataFrame()

# load data to database

def load_to_database(df, table_name):
    try:
        print(f"loading data into database table {table_name}...")
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            df.to_sql(table_name, connection, if_exists="append", index=False)
        print(f"data loaded successfully into {table_name}.")
    except Exception as e:
        print(f"error loading data into database: {e}")

# main etl process

def etl_process():
    print("starting etl process...")
    
    # extract
    
    api_data = extract_from_api()
    csv_data = extract_from_csv()

    # combine data sources
    
    combined_data = pd.concat([api_data, csv_data], ignore_index=True)

    # transform
    
    transformed_data = transform_data(combined_data)

    # load
    
    load_to_database(transformed_data, "integrated_data")

    print("etl process complete.")

# entry point

if __name__ == "__main__":
    etl_process()
