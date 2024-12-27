import requests
import pandas as pd
import time
import os

# configure api and file paths

API_URL = .
SAVE_PATH = "real_time_data.csv"

# function to fetch data from api

def fetch_data():
    try:
        print("fetching data from api...")
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        print("data fetched successfully.")
        return data
    except requests.exceptions.RequestException as e:
        print(f"error fetching data: {e}")
        return None

# function to process and save data

def process_and_save_data(data):
    if not data:
        print("no data to process.")
        return

    try:
        
        # convert json to dataframe
        
        df = pd.DataFrame(data)
        
        # if file exists, append to it; otherwise, create a new file
        
        if os.path.exists(SAVE_PATH):
            existing_df = pd.read_csv(SAVE_PATH)
            df = pd.concat([existing_df, df], ignore_index=True)

        # save to file
        
        df.to_csv(SAVE_PATH, index=False)
        print(f"data processed and saved to {SAVE_PATH}")
    except Exception as e:
        print(f"error processing or saving data: {e}")

# real-time data ingestion loop

def real_time_ingestion(interval=60):
    print("starting real-time data ingestion...")
    while True:
        data = fetch_data()
        process_and_save_data(data)
        print(f"waiting {interval} seconds for the next fetch...")
        time.sleep(interval)

# entry point

if __name__ == "__main__":
    try:
        real_time_ingestion(interval=300)  # fetch data every 5 minutes
    except KeyboardInterrupt:
        print("real-time data ingestion stopped.")

