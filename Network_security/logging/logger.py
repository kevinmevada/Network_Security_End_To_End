import logging
import os
from datetime import datetime

# Create a log file name using current time
log_filename = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a folder called "logs" in the current project
logs_folder_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_folder_path, exist_ok=True)

# Full path of the log file
log_file_path = os.path.join(logs_folder_path, log_filename)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
)
