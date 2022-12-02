from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ

# Sqlite
# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# PostgreSQL
# SQLALCHEMY_DATABASE_URL = "postgresql://{id}:{password}@localhost/{database_name}"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# mysql
MYSQL_USER = environ.get('MYSQL_USER')
MYSQL_PASSWORD = environ.get('MYSQL_PASSWORD')
MYSQL_DB = environ.get('MYSQL_DB')
MYSQL_ADDR = environ.get('MYSQL_ADDR')
MYSQL_PORT = environ.get('MYSQL_PORT')
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_ADDR}:{MYSQL_PORT}/{MYSQL_DB}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
