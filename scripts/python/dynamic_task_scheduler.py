import schedule
import time
import subprocess
from datetime import datetime

# define tasks with priority levels

TASKS = [
    {"name": "workflow_orchestrator.py", "priority": 1, "interval": "daily", "time": "00:00"},
    {"name": "etl_automation.py", "priority": 2, "interval": "hourly", "time": None},
    {"name": "real_time_data_ingestion.py", "priority": 3, "interval": "minutes", "time": 15},  # every 15 minutes
]

# function to run a task

def run_task(script_name):
    try:
        print(f"running task: {script_name}")
        subprocess.run(["python", script_name], check=True)
        print(f"task {script_name} completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"error: task {script_name} failed with exit code {e.returncode}")
    except Exception as e:
        print(f"unexpected error while running task {script_name}: {e}")

# schedule tasks dynamically

def schedule_tasks():
    print("scheduling tasks dynamically...")
    for task in TASKS:
        if task["interval"] == "daily":
            schedule.every().day.at(task["time"]).do(run_task, task["name"])
        elif task["interval"] == "hourly":
            schedule.every().hour.do(run_task, task["name"])
        elif task["interval"] == "minutes":
            schedule.every(task["time"]).minutes.do(run_task, task["name"])
    print("all tasks scheduled successfully.")

# monitor and run scheduled tasks

def run_scheduler():
    schedule_tasks()
    print("dynamic task scheduler initialized. waiting for tasks...\n")
    while True:
        schedule.run_pending()
        time.sleep(1)

# entry point

if __name__ == "__main__":
    try:
        print("starting dynamic task scheduler...")
        run_scheduler()
    except KeyboardInterrupt:
        print("dynamic task scheduler stopped manually.")
