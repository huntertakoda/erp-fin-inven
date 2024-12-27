import schedule
import time
import subprocess

# helper function to run the orchestrator script

def run_orchestrator():
    try:
        print("starting workflow orchestrator...")
        subprocess.run(["python", "workflow_orchestrator.py"], check=True)
        print("workflow orchestrator completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"error: workflow orchestrator failed with exit code {e.returncode}")
        print(f"stderr: {e.stderr if e.stderr else 'no stderr captured'}")
    except Exception as e:
        print(f"unexpected error while running orchestrator: {e}")

# schedule the orchestrator to run daily at midnight

schedule.every().day.at("00:00").do(run_orchestrator)

# run the scheduler loop

if __name__ == "__main__":
    print("scheduler initialized. waiting for tasks...\n")
    while True:
        schedule.run_pending()
        time.sleep(1)
