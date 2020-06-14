from flask import Flask, jsonify
from flask_cors import CORS
from rotasTreinador import rotas_treinador
from rotasPokemom import rotas_pokemoms

app = Flask(__name__)
#cors = CORS(app, resources={r"/*": {"origins": "*","methods": "*"}})
CORS(app)

app.register_blueprint(rotas_treinador)
app.register_blueprint(rotas_pokemoms)

@app.route('/')
def hello_world():
    return jsonify({'status':'ok'})

if __name__ == '__main__':
    app.run(debug=True)
