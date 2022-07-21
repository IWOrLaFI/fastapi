import databases
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:changeme@postgres:5432/'
SQLALCHEMY_DATABASE_URL = 'postgresql://worlaf:qwerty@postgres:5432/fast'
metadata = MetaData()
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

Base = declarative_base()


def get_db():
    _db = databases.Database(SQLALCHEMY_DATABASE_URL)
    return _db 


def get_session() -> SessionLocal:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def create_db():
    Base.metadata.create_all(create_engine('sqlite:///users.sqlite3'))
    return print('db_create')
