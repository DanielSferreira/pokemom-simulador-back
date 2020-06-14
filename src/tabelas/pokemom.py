from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class pokemom(Base):
    __tablename__ = 'pokemom'

    id = Column(Integer, primary_key = True,autoincrement=True )
    id_pokedex = Column(Integer)
    pokemom_nome = Column(String)
    id_treinador = Column(Integer)
    nivel_pokemom = Column(Integer)

    def __init__(self, novo_pokemom):
        self.id_pokedex = novo_pokemom.id_pokedex
        self.pokemom_nome = novo_pokemom.pokemom_nome
        self.id_treinador = novo_pokemom.id_treinador
        self.nivel_pokemom = novo_pokemom.nivel_pokemom
