from flask import Flask, request, Response
from flask_restful import Resource, Api
import uuid
import random
import json

uuid.uuid4()

app = Flask(__name__)
api = Api(app)

# Lista de partidas
gameList = []
# Lista de jogadas
movementList = []

# Lista de jogadas
movement = {
    'id':'fbf7d720-df90-48c4-91f7-9462deafefb8',
    'player':'X',
    'position': {
        'x':0,
        'y':1
    }
}

# Inicia a partida - Sorteio quem vai começar
class postGame(Resource):
    # Criar nova partida - POST /game/
    def post(self):
        # Sorteio primeiro jogador
        firstPlayer = random.choice(['X', 'O'])
        # Gerar Id da partida - Persistencia de dados
        dados = json.loads(request.data)
        dados['id'] = str(uuid.uuid4())
        dados['firstPlayer'] = firstPlayer
        gameList.append(dados)
        return gameList
    # Listar partidas - GET /game/
    def get(self):
        return gameList

# Salva jogadas
class postMovement(Resource):

    # POST - /game/<id>
    def post(self, id, player, position):
        # Buscar partida pelo id
        # Se a partida não existir: {'msg':'Partida não existe'
       for item in gameList:
            if (id == item['id']):
                dados = json.loads(request.data)
                dados['id'] = id
                dados['player'] = player
                dados['position'] = position
                movementList.append(dados)
                # response = {'status':'200', 'msg': 'Jogada realizada com sucesso'}
                return Response(status=201)
            else:
                response = {'msg': 'Partida não encontrada'}
                return response
#      Caso nao seja o turno do jogador: response = {'msg': 'Não é turno do jogador'}
#      Final de jogo: response = {'msg': 'Partida finalizada', 'winner':'X'}
#      Empate (Velha): response = {'msg': 'Partida finalizada', 'winner':'Draw'}

api.add_resource(postGame, '/game/')
api.add_resource(postMovement, '/game/<string:id>/<string:player>/<string:position>')

if __name__ == '__main__':
    app.run(debug=True)