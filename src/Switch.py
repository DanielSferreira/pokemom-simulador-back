from .tabelas.aluno import aluno
from .tabelas.pokemom import pokemom
from .tabelas.pokeList import pokeList
from .tabelas.treinador import treinador

tabelas = { 'aluno': aluno, 'pokemom': pokemom, 'treinador': treinador, 'pokeList':pokeList }

def getInstanciaTabela(tabela_nome, objeto_instancia):
    for key in tabelas:
        if tabela_nome == key:
            obj = tabelas[key](objeto_instancia)
    return obj

def getTabela(tabela_nome):
    for key in tabelas:
        if tabela_nome == key:
            obj = tabelas[key]
    return obj
