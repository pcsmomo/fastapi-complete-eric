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
POSTGRES_USER = environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD')
POSTGRES_DB = environ.get('POSTGRES_DB')
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres-db/{POSTGRES_DB}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# mysql
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{id}:{password}@127.0.0.1:3306/{database_name}"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
