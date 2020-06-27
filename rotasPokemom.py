from flask import Blueprint, jsonify, request
from src.models.pokemom import pokemom
from src.models.treinador import treinador
from src.models.pokeList import pokeList
from src.crud import execute, getAllByNameTable, getPokemomByColumnName, getTreinadorByColumnName
import requests

rotas_pokemoms = Blueprint('urls2', __name__)

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
        print(res) 
    except Exception as e:
        res = ['Erro na busca']
    return jsonify({'id_pokedex': res.id_pokedex, "pokemom_nome": res.pokemom_nome})
    

def getTreinadoresValores(column,value):
    res = getTreinadorByColumnName(column,value)
    try:
        response = res
    except AttributeError as error:
        response = ["Não houve retorno da coluna {} com o valor: {}".format(column,value)]
        
    return jsonify(response)

@rotas_pokemoms.route('/pokemom/setPokemomForTrainer/', methods = ['POST'])
def setPokemomForTrainer():
    user_data = request.get_json() # 
    print(user_data)
    try:
        
        idPokedex = user_data['id_pokedex']
        pokemomNome = user_data['pokemom_nome']
        idTrainer = user_data['id_treinador']
        nivelPokemom = user_data['nivel_pokemom']
        
        try:
            res = execute('pokemom', pokemom(idPokedex, pokemomNome, idTrainer, nivelPokemom))
        
        except Exception:
            return ['Erro ao salvar no banco de dados']
        
    except Exception as e:
       res = [{'Erro':str(e)}]
            
    return jsonify(res)
