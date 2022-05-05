import datetime

from logging import Logger, NOTSET, Formatter, FileHandler, StreamHandler

# It creates a logger object with the given name and level
class ILogger(Logger):
    def __init__(self, name: str, file: str = None, level=NOTSET):
        """
        This function sets the logger object.  It takes in a logger name and a logger level and returns an integer

        Args:
          logger_name (str): The name of the logger.
          logger_level (str): The level of logging you want to see. This can be one of the following:'CRITICAL',
          'DEBUG', 'ERROR', 'FATAL','INFO','NOTSET', 'WARNING'
        Defaults to INFO

        Returns:
          The return value is the exit code of the function.
        """
        Logger.__init__(self, name, level)
        formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        if file:
            fileHandler = FileHandler(file, mode="a")
            fileHandler.setFormatter(formatter)

        streamHandler = StreamHandler()
        streamHandler.setFormatter(formatter)

        self.addHandler(fileHandler)
        self.addHandler(streamHandler)
