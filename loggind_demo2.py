import logging

logging.basicConfig(filename="/Users/ajayvidekar/Desktop/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s ',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG
                    ) # add level to print debug and info messages to log file

# self.logger = logging.getLogger()
# self.logger.setLevel(logging.DEBUG)

# by default debug and info messages not printed on console
logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")

