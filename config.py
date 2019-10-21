import logging
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv, find_dotenv
import os
import sqlalchemy as sa
from urllib.parse import quote_plus as urlquote
from sqlalchemy.ext.declarative import declarative_base


class Config(object):

    conn = ''
    self.Base = declarative_base()

    def __init__(self):

        load_dotenv(find_dotenv('.env'))
        self.APP_ROOT = os.path.dirname(os.path.abspath(__file__))
        self.LOG_LEVEL = logging.DEBUG
        self.DB_HOST = os.getenv('DB_HOST', 'localhost')
        self.DB_USER = os.getenv('DB_USER', 'admin')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD', 'abc123')
        self.DB_PORT = os.getenv('DB_PORT', 27017)
        self.DB_NAME = os.getenv('DB_NAME', 'compensar')

    def create_engine(self):
        """connect to Sql Server"""
        try:
            connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=tcp:' + \
                self.DB_HOST + ';DATABASE=' + self.DB_NAME + \
                ';UID=' + self.DB_USER + \
                ';PWD=' + self.DB_PASSWORD
            connection_string = urlquote(connection_string)
            connection_string = "mssql+pyodbc:///?odbc_connect=%s" % connection_string
            engine = sa.create_engine(
                'mssql+pyodbc:///?odbc_connect=%s' % connection_string)

            engine = sa.create_engine(connection_string)
            self.conn = engine.connect()

        except SQLAlchemyError as error:
            error = str(error.__dict__['orig'])
            print(error)

        return engine
