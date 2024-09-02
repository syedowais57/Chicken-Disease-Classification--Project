import os
import sys
import logging

# Define logging format
logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

# Define log directory and file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Writes logs to a file
        logging.StreamHandler(sys.stdout)    # Prints logs to console
    ]
)

# Create logger
logger = logging.getLogger("cnnClassifierLogger")
