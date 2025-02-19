import logging

class LoggerExample:
    def __init__(self, log_file="app.log"):
        # Step 1: Create a logger
        self.logger = logging.getLogger("CustomLogger")
        # a = logging.addHandler
        self.logger.setLevel(logging.DEBUG)  # Capture all logs (DEBUG and higher)

        # Step 2: Create console handler for ERROR level logs
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)

        # Step 3: Create file handler for DEBUG level logs
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # Step 4: Define log format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Step 5: Add handlers to the logger
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def log_messages(self):
        self.logger.debug("This is a DEBUG message (file only)")
        self.logger.info("This is an INFO message (file only)")
        self.logger.warning("This is a WARNING message (file only)")
        self.logger.error("This is an ERROR message (file & console)")
        self.logger.critical("This is a CRITICAL message (file & console)")


if __name__ == "__main__":
    logger_example = LoggerExample()
    logger_example.log_messages()
