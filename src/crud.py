from .Switch import getInstanciaTabela, getTabela
from src import db
from sqlalchemy import exc

def execute(tbl,obj):
    try:
        objeto_persist = getInstanciaTabela(tabela_nome=tbl, objeto_instancia=obj)
        db.session.add(objeto_persist)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        return e
    else:
        print("Olá")
        return {'status':'ok'}

def getAllByNameTable(tbl):
    
    try:
        res = db.session.query(getTabela(tbl)).all()
    except exc.SQLAlchemyError as e:
        return e
    else:
        return res

def getTreinadorByColumnName(index,valor):
    print('aqui 0')
    tbl = getTabela('treinador')
    try:
        if index == 'nome_treinador': 
            res = db.session.query(tbl).filter(tbl.nome_treinador == valor).first()
            print('aqui 1')
        elif index == 'regiao': 
            print('aqui 2')
            res = db.session.query(tbl).filter(tbl.regiao == valor).first()
        elif index == 'id_de_treinador': 
            print('aqui 3')
            res = db.session.query(tbl).filter(tbl.id_de_treinador == valor).first()
    except exc.SQLAlchemyError as e:
        print('aqui 4')
        return e
    else:
        print('aqui 5')
        return res

def getPokemomByColumnName(index,valor):
    tbl = getTabela('pokeList')
    try:
        if index == 'id_pokedex': 
            res = db.session.query(tbl).filter(tbl.id_pokedex == valor).first()
        elif index == 'pokemom_nome': 
            res = db.session.query(tbl).filter(tbl.pokemom_nome == valor).first()
    except exc.SQLAlchemyError as e:
        return e
    else:
        return res

def getPokemomsByColumnName(index,valor):
    tbl = getTabela('pokemom')
    try:
        if index == 'id_pokedex': 
            res = db.session.query(tbl).filter(tbl.id_pokedex == valor).all()
        elif index == 'pokemom_nome': 
            res = db.session.query(tbl).filter(tbl.pokemom_nome == valor).all()
        elif index == 'id_treinador': 
            res = db.session.query(tbl).filter(tbl.id_treinador == valor).all()
        elif index == 'nivel_pokemom': 
            res = db.session.query(tbl).filter(tbl.nivel_pokemom == valor).all()
    except exc.SQLAlchemyError as e:
        return e
    else:
        return res
