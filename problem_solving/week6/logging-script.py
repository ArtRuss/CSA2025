from getpass import getpass
import logging
import sys

from input import setup, display

logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

class SingletonLogger():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonLogger, cls).__new__(cls)
            cls._instance._logger = logging.getLogger("my.singleton.logger")
            cls._instance._logger.setLevel(logging.INFO)
        if not cls._instance._logger.hasHandlers():
            file_handler = logging.FileHandler('myapp.log')
            stream_handler = logging.StreamHandler(sys.stdout)
        cls._instance._logger.addHandler(file_handler)
        cls._instance._logger.addHandler(stream_handler)
        return cls._instance
    
    def info(self, msg):
        self._logger.info(msg)
    
    def debug(self, msg):
        self._logger.debug(msg)
    
    def error(self, msg):
        self._logger.error(msg)
    def warning(self, msg):
        self._logger.warning(msg)
            
def main():
    username = ""
    password = ""
    age = ""
    while not username or not password or not age: 
        logger.info("Input a valid username, password and age.")
        username, password, age = setup()

    display(username=username, password=password, age=age)

if __name__ == "__main__":
    main()
