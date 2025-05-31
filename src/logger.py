import logging
import os
from datetime import datetime

log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

log_file = f"{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(log_dir, log_file)

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)
