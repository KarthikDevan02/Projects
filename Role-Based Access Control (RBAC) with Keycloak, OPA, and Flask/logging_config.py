import logging

# Logging configuration
logging.basicConfig(filename='access.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
