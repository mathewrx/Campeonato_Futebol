from flask import Flask, json, jsonify
from flask import request
from prog import Partida, Campeonato
from playhouse.shortcuts import model_to_dict


app = Flask(__name__)


@app.route('/', methods=['GET'])
def inicio():
    return "BLA"


@app.route('/listar_campeonato')
def listar_campeonato():
    # converte para pessoa para inserir em uma lista json
    campeonato= list(map(model_to_dict, Campeonato.select()))
    # adiciona à lista json um nome
    response = jsonify({"campeonato": campeonato})
    # informa que outras origens podem acessar os dados desde servidor/serviço
    response.headers.add('Access-Control-Allow-Origin', '*')
    # retorno!
    return response

@app.route('/listar_partida')
def listar_partida():
    # converte para pessoa para inserir em uma lista json
    partida= list(map(model_to_dict, Partida.select()))
    # adiciona à lista json um nome
    response = jsonify({"partida": partida})
    # informa que outras origens podem acessar os dados desde servidor/serviço
    response.headers.add('Access-Control-Allow-Origin', '*')
    # retorno!
    return response

app.run(debug=True, port=4999)