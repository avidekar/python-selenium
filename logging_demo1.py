import logging

logging.basicConfig(filename="/Users/ajayvidekar/Desktop/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s ',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG) # add level to print debug and info messages to log file

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# by default debug and info messages not printed on console
logger.debug("This is a debug message")
logger.info("This is a info message")
logger.warning("This is a warning message")
logger.error("This is a error message")
logger.critical("This is a critical message")
