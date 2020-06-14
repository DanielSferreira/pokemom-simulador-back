from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class treinador(Base):
    __tablename__ = 'treinador'

    id = Column(Integer, primary_key = True, autoincrement=True)
    nome_treinador = Column(String)
    regiao = Column(String)
    id_de_treinador = Column(Integer)

    def __init__(self, novo_treinador):
        self.nome_treinador = novo_treinador.nome_treinador
        self.regiao = novo_treinador.regiao
        self.id_de_treinador = novo_treinador.id_de_treinador
