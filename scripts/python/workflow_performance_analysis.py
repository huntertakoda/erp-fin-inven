import time
import logging
import pandas as pd
from datetime import datetime

# configure log file for performance data

LOG_FILE = "performance_logs.csv"

# setup logging

logging.basicConfig(
    filename="workflow_performance.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# log performance data to a CSV file

def log_performance_data(script_name, execution_time):
    try:
        
        # prepare data entry
        
        data = {
            "timestamp": [datetime.now()],
            "script_name": [script_name],
            "execution_time_seconds": [execution_time],
        }

        # write or append to csv
        if not os.path.exists(LOG_FILE):
            pd.DataFrame(data).to_csv(LOG_FILE, index=False)
        else:
            pd.DataFrame(data).to_csv(LOG_FILE, mode="a", header=False, index=False)

        logging.info(f"performance data logged for {script_name}.")
    except Exception as e:
        logging.error(f"error logging performance data: {e}")

# measure performance of a script

def measure_performance(script_name):
    try:
        print(f"measuring performance for {script_name}...")
        start_time = time.time()

        # simulate running the script
        
        subprocess.run(["python", script_name], check=True)

        end_time = time.time()
        execution_time = round(end_time - start_time, 2)
        print(f"{script_name} completed in {execution_time} seconds.")

        # log performance data
        
        log_performance_data(script_name, execution_time)
    except Exception as e:
        logging.error(f"error measuring performance for {script_name}: {e}")
        print(f"error running {script_name}: {e}")

# analyze performance logs

def analyze_performance_logs():
    try:
        print("analyzing performance logs...")
        if not os.path.exists(LOG_FILE):
            print("no performance data available.")
            return

        # load performance data
        
        df = pd.read_csv(LOG_FILE)

        # calculate summary statistics
        
        summary = df.groupby("script_name").agg(
            total_runs=("execution_time_seconds", "count"),
            average_time=("execution_time_seconds", "mean"),
            max_time=("execution_time_seconds", "max"),
            min_time=("execution_time_seconds", "min"),
        ).reset_index()

        print("performance summary:\n", summary)
    except Exception as e:
        logging.error(f"error analyzing performance logs: {e}")
        print(f"error analyzing logs: {e}")

# entry point

if __name__ == "__main__":
    import subprocess  

    print("starting workflow performance analysis...")
    
    # test performance measurement
    
    test_scripts = [
        "workflow_orchestrator.py",
        "etl_automation.py",
        "real_time_data_ingestion.py",
    ]

    for script in test_scripts:
        measure_performance(script)

    # analyze performance data
    
    analyze_performance_logs()

    print("workflow performance analysis complete.")
