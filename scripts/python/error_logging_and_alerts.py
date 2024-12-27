import logging
from smtplib import SMTP

# configure log file and email settings

LOG_FILE = "error_logs.log"
EMAIL_SMTP_SERVER = .
EMAIL_PORT = .
EMAIL_SENDER = .
EMAIL_RECIPIENT = .
EMAIL_PASSWORD = .

# setup logging

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.ERROR,
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

# function to log an error

def log_error(script_name, error_message):
    error_message_full = f"error in script {script_name}: {error_message}"
    logging.error(error_message_full)
    send_email_alert(subject=f"Pipeline Error in {script_name}", message=error_message_full)

# simulate running a script with error logging

def run_script_with_error_logging(script_name, simulate_error=False):
    try:
        print(f"running {script_name}...")
        if simulate_error:
            raise Exception(f"simulated error in {script_name}")
        print(f"{script_name} completed successfully.")
    except Exception as e:
        log_error(script_name, str(e))

# main function for testing

if __name__ == "__main__":
    print("starting error logging and alerts test...")
    
    # test with successful script
    
    run_script_with_error_logging("test_script_1.py", simulate_error=False)

    # test with simulated error
    
    run_script_with_error_logging("test_script_2.py", simulate_error=True)

    print("error logging and alerts test complete. check logs and email for details.")
