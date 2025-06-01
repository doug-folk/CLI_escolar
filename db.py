from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Database:
    def __init__(self.engine = create_engine("postgresql://usuario:senha@localhost/escola"):
        self.engine = create_engine(url, echo=False, future=True)
        self.Session = sessionmaker(bind=self.engine, future=True)

    def criar_tabelas(self):
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()

db = Database()
