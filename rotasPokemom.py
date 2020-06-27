from flask import Blueprint, jsonify, request
from src.models.pokemom import pokemom
from src.models.treinador import treinador
from src.models.pokeList import pokeList
from src.crud import execute, getAllByNameTable, getPokemomByColumnName, getTreinadorByColumnName
import requests

rotas_pokemoms = Blueprint('urls2', __name__)
response = []

@rotas_pokemoms.route('/pokemom/getPokemomId/<int:idPoke>/')
def getPokemomId(idPoke):
    pokemom = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(idPoke))
    nome = pokemom.json()['name']
    return '<h2>{}</h2>'.format(nome)

@rotas_pokemoms.route('/pokemom/listPokemom/')
def listPokemom():
    res = []
    try:
        getData = getAllByNameTable('pokeList')
        for i in getData:
            res.append({
                'id_pokedex': i.id_pokedex,
                'pokemom_nome': i.pokemom_nome
            })
    except Exception as e:
        res = ['Erro na busca']

    return jsonify(res)

@rotas_pokemoms.route('/pokemom/getBy/<column>/<value>')
def getByColumnValue(column,value):
    
    try:
        res = getPokemomByColumnName(column,value)
        response = {'id_pokedex': res.id_pokedex, 'pokemom_nome': res.pokemom_nome }

    except Exception as e:
        response = [{'id_pokedex': 'error', "pokemom_nome": 'error'}]

    return jsonify(response)
    

def getTreinadoresValores(column,value):
    try:
        response = getTreinadorByColumnName(column,value)
    except AttributeError as error:
        response = ["Não houve retorno da coluna {} com o valor: {}".format(column,value)]
        
    return jsonify(response)

@rotas_pokemoms.route('/pokemom/setPokemomForTrainer/', methods = ['POST'])
def setPokemomForTrainer():
    
    try:
        user_data = request.get_json()
        
        idPokedex = user_data['id_pokedex']
        pokemomNome = user_data['pokemom_nome']
        idTrainer = user_data['id_treinador']
        nivelPokemom = user_data['nivel_pokemom']
        
        try:
            response = execute('pokemom', pokemom(idPokedex, pokemomNome, idTrainer, nivelPokemom))
        
        except Exception:
            response =  {'status':'error em salvar'}
        
    except Exception as e:
       response = [{'Erro':str(e)}]
            
    return jsonify(response)
