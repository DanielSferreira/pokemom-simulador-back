from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class pokeList(Base):
    __tablename__ = 'pokeList'

    id_pokedex = Column(Integer, primary_key = True)
    pokemom_nome = Column(String)

    def __init__(self, novo_pokemom):
        self.id_pokedex = novo_pokemom.id_pokedex
        self.pokemom_nome = novo_pokemom.pokemom_nome
