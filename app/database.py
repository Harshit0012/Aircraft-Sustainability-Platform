from sqlalchemy import create_engine, text, func
from sqlalchemy.orm import declarative_base, sessionmaker, Session
# from .config import setting

# SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}"
SQLALCHEMY_DATABASE_URL = f"sqlite:///data/database.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()

# con = next(get_db())
# data = con.execute(text('PRAGMA database_list')).fetchall()
# print(data)

# con = next(get_db())
# data = con.execute(text('show databases')).fetchall()
# db = SessionLocal()