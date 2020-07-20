# Jogo da Velha Multiplayer

O objetivo deste projeto é desenvolver uma api para um jogo multiplayer de Jogo da Velha.

O projeto possui dois arquivos:
  - Um baseado em API's com chamadas POST utilizando a linguagem de programação Python e o framework Flask e Flask-Restful
  - Outro com a lógica básica para rodar no console.

Curso base para a construção deste projeto:
Digital Innovation - Desenvolvimento Avançado de REST-API com Flask
https://web.digitalinnovation.one/course/desenvolvimento-avancado-de-rest-api-com-flask/

## Python 3

É necessário ter o Python 3 instalado. Faça o download aqui: https://www.python.org/downloads/

## Dependências

    click==7.1.2
    Flask==1.1.2
    itsdangerous==1.1.0
    Jinja2==2.11.2
    MarkupSafe==1.1.1
    Werkzeug==1.0.1
    Flask-RESTful==0.3.8
    
    ### `pip freeze > Requirements.txt`

## API's

### POST - /game/
Essa chamada criara uma nova partida e retornará o id da partida criada. 
Além do id ele vai sortear qual jogador ira começar a partida o "X" ou o "O".

    {
      "id" : "fbf7d720-df90-48c4-91f7-9462deafefb8",
      "firstPlayer": "X"
    }


### POST - /game/{id}/
Essa chamada fará o movimento de cada jogador.
A partir da id da partida informada, esta chamada salva o player e a posição da jogada.

      {
        "id" : "fbf7d720-df90-48c4-91f7-9462deafefb8",
        "player": "X",
        "position": {
          "x": 0,
          "y": 1
        }
      }

## Jogar no Console
Execute o arquivo "Methods.py" para jogá-lo no prompt de comando. 
O jogo exibe quem é o jogador da vez.
O jogador deve falar a posição que deseja ocupar baseado em x e y:

       (x=2 y=2) | (x=1 y=2) | (x=0 y=2)
      -----------|-----------|----------
       (x=2 y=1) | (x=1 y=1) | (x=0 y=1)
      -----------|-----------|----------
       (x=2 y=0) | (x=1 y=0) | (x=0 y=0)
