import os
import time
import logging
from datetime import datetime
from smtplib import SMTP

# configure log file and email settings

LOG_FILE = "pipeline_monitor.log"
EMAIL_SMTP_SERVER = .
EMAIL_PORT = .
EMAIL_SENDER = .
EMAIL_RECIPIENT = .
EMAIL_PASSWORD = .

# setup logging

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# function to send email alerts

def send_email_alert(subject, message):
    try:
        with SMTP(EMAIL_SMTP_SERVER, EMAIL_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            email_message = f"Subject: {subject}\n\n{message}"
            smtp.sendmail(EMAIL_SENDER, EMAIL_RECIPIENT, email_message)
            logging.info("email alert sent successfully.")
    except Exception as e:
        logging.error(f"failed to send email alert: {e}")

# function to check log for errors

def check_for_errors(log_file):
    try:
        with open(log_file, "r") as file:
            lines = file.readlines()
        errors = [line for line in lines if "error" in line.lower()]
        if errors:
            logging.warning("errors detected in the pipeline log.")
            send_email_alert(
                subject="Pipeline Error Detected",
                message="\n".join(errors),
            )
        else:
            logging.info("no errors detected in the pipeline log.")
    except FileNotFoundError:
        logging.error(f"log file {log_file} not found.")
    except Exception as e:
        logging.error(f"unexpected error while checking log file: {e}")

# function to monitor pipeline scripts

def monitor_pipeline(script_paths):
    for script in script_paths:
        if not os.path.exists(script):
            logging.error(f"script {script} is missing.")
            send_email_alert(
                subject="Pipeline Script Missing",
                message=f"the script {script} is missing from the directory.",
            )
        else:
            logging.info(f"script {script} is present.")

# main monitor process

def pipeline_monitor():
    logging.info("starting pipeline monitor...")
    script_paths = [
        "workflow_orchestrator.py",
        "etl_automation.py",
        "real_time_data_ingestion.py",
        "schedule_workflows.py",
    ]

    while True:
        
        # check for script presence
        
        monitor_pipeline(script_paths)

        # check the log file for errors
        
        check_for_errors(LOG_FILE)

        logging.info("pipeline monitor iteration complete. waiting for the next check...")
        time.sleep(300)  

if __name__ == "__main__":
    try:
        pipeline_monitor()
    except KeyboardInterrupt:
        logging.info("pipeline monitor stopped manually.")
