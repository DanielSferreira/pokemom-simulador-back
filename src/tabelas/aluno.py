from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class aluno(Base):
    __tablename__ = 'aluno'

    id = Column(Integer, primary_key = True, autoincrement=True)
    nome = Column(String)
    matricula = Column(String)
    serie = Column(Integer)

    def __init__(self, novo_aluno):
        self.nome = novo_aluno.nome
        self.matricula = novo_aluno.matricula
        self.serie = novo_aluno.serie