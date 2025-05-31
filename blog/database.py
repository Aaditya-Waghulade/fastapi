#1.Importing engine from sqlalchemy and declarative_base from sqlalchemy.ext.declarative, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#2. Defining the connection url of the database
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

#3. creating variable engine and storing connection into it
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

#4. Now lastly create a session
SessionLocal = sessionmaker(bind = engine,autocommit=False,autoflush=False)

#5. Defining Base class using declarative_base
Base = declarative_base()

#6. Now making "models.py(tables and enities)" file to create the tables and entities in the database.
