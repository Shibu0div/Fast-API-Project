from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
db_url = "mysql+mysqlconnector://root:SHIBU@127.0.0.1:3306/shibu"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False,autoflush=False,bind=engine)