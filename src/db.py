from sqlalchemy import create_engine, MetaData, Column, Integer, String
from sqlalchemy.orm import sessionmaker

db_string = "postgres://postgres:5978321@localhost/Coxinha"

DB = create_engine(db_string)
meta = MetaData()
meta.reflect(bind=DB)
Session = sessionmaker(bind=DB)
session = Session()
