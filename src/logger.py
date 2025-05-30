import logging
import os
from datetime import datetime

log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)
print("Logs folder exists?", os.path.exists(log_dir))



log_file = f"{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(log_dir, log_file)
print("Log file path:", LOG_FILE_PATH)
print("Does log file exist?", os.path.exists(LOG_FILE_PATH))

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

def divide(a, b):
    try:
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result
    except Exception as e:
        logging.error("Error occurred during division", exc_info=True)

# Example usage
divide(10, 2)
divide(5, 0)