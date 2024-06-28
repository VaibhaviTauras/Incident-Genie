import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool

from logger.logger import logger


# Declare the database ORM class
Base = declarative_base()


class DatabaseManager:
    """
    Create database Engine and Session
    """
    def __init__(self, username: str, password: str, hostname: str, port: str, db_name: str):
        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port
        self.db_name = db_name

    def database_url(self):
        DATABASE_URL = f"postgresql+psycopg2://{self.username}:{self.password}@{self.hostname}:{self.port}/{self.db_name}"
        return DATABASE_URL

    def db_session(self):
        engine = create_engine(
            self.database_url(),
            pool_size=100,
            max_overflow=200,
            pool_recycle=300
        )
        session = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine
        )
        return session, engine

    def service_db_session(self):
        engine = create_engine(
            self.database_url(),
            poolclass=NullPool
        )
        session = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine
        )
        return session, engine

    def create_database(self):
        try:
            #establishing the connection
            conn = psycopg2.connect(
            database="postgres", user=self.username, password=self.password, host=self.hostname, port=self.port
            )
            conn.autocommit = True

            #Creating a cursor object using the cursor() method
            cursor = conn.cursor()

            #Preparing query to create a database
            sql = f'''CREATE database "{self.db_name}";'''

            #Creating a database
            response = cursor.execute(sql)
            logger.info("Database created successfully........")

            #Closing the connection
            conn.close()
            return response
        except ProgrammingError as e:
            logger.error(f"Error: {e}")
        finally:
            conn.close()
