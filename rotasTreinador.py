from flask import Blueprint, jsonify, request
from src.models.treinador import treinador
from src.models.pokemom import pokemom
from src.crud import execute, getAllByNameTable, getTreinadorByColumnName, getPokemomsByColumnName

rotas_treinador = Blueprint('urls', __name__)

@rotas_treinador.route('/treinador/novo', methods = ['POST'])
def newTreinador():
    try:
        user_data = request.get_json() # 
        print(user_data)
    except Exception as e:
        response = 'erro ao resgatar'
        print(response)
    try:
        res = execute('treinador', treinador(user_data['nome_treinador'],user_data['regiao'],user_data['id_de_treinador']))
        response = "Sucesso"
    except Exception:
        print('erro ao salvar')
        response = 'erro ao salvar'
    return jsonify({'status':response})

@rotas_treinador.route('/treinadores/all')
def getTreinadores():
    data = []
    res = getAllByNameTable('treinador')
    for i in res:
        data.append([i.id_de_treinador, i.nome_treinador]);
    return jsonify(data)

@rotas_treinador.route('/treinadores/<key>/<value>/')
def getTreinadorValores(key,value):
    res = getTreinadorByColumnName(key,value)
    try:
        response = res.nome_treinador
    except AttributeError as error:
        response = ["Não houve retorno da coluna {} com o valor: {}".format(key,value)]
        
    return jsonify(response)

@rotas_treinador.route('/pokemomsByTreinador/<nome>/')
def getPokemonsByTreinador(nome):
    data = []
    treinador = getTreinadorByColumnName('nome_treinador',nome)
    try:
        print(treinador.id_de_treinador)
    except Exception:
        data = ["Treinador não achadado HAHA"]
    else:
        try:    
            res = getPokemomsByColumnName('id_treinador',treinador.id_de_treinador)
        except Exception:
            data = ["Treinador não possui Pokemom"]
        else:
            for linha in res:
                data.append(linha.pokemom_nome)
    return jsonify(data)
