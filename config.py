import logging
from dotenv import load_dotenv, find_dotenv
import os


class Config(object):

    def __init__(self):

        load_dotenv(find_dotenv('.env'))
        self.APP_ROOT = os.path.dirname(os.path.abspath(__file__))
        self.LOG_LEVEL = logging.DEBUG
        self.DB_HOST = os.getenv('DB_HOST', 'localhost')
        self.DB_USER = os.getenv('DB_USER', 'admin')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD', 'abc123')
        self.DB_PORT = os.getenv('DB_PORT', 27017)
        self.DB_NAME = os.getenv('DB_NAME', 'compensar')
