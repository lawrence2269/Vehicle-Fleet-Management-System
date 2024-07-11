from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL

from decouple import config

# Creating URL object
MYSQL_DATABASE_URL = URL.create(
    config('DRIVER_NAME'),
    username=config('USERNAME'),
    password=config('PASSWORD'),
    host=config('HOST'),
    database=config('DATABASE'),
    port=config('PORT')
)

engine = create_engine(MYSQL_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
