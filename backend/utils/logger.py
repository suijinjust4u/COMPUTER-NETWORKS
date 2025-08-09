import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s"
)

def get_logger(name=None):
    return logging.getLogger(name)
