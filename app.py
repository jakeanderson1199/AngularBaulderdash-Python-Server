from flask import Flask,render_template,jsonify, make_response,json,request
from datetime import datetime
import re
from game_class import *
from player_class import *
from to_dict import *
from Answer_class import Answer
from flask_cors import CORS

app = Flask(__name__)

CORS(app)



@app.route("/")
def home():
    return "Mom is a noob"



    





@app.route("/games/<owner_name>", methods=['POST'])
def postGame(owner_name):
    ##global game
    game = Game()
    
    game.owner_name = owner_name
    game.new_turn()
    games.append(game)
    content = todict(game)
    print(game.owner_name)
    return make_response(jsonify(content))
    
@app.route("/games")
def getGames():
    ##games = []
    ##games.append(game) 

    return make_response(jsonify(todict(games)))


@app.route("/games/<owner_name>/players/<player_name>/answer", methods=['POST'])
def postAnswer(owner_name,player_name):
    content = request.get_json()
    answer = content['answer']
    for g in games:
        if g.owner_name == owner_name:
            game = g

    for person in game.players:
        if person.name == player_name:
            person.answer = Answer(person.id)
            person.answer.text = answer
            game.turn.answers.append(person.answer)

    
    return make_response(jsonify(todict(game)))


@app.route("/games/<owner_name>/players/<player_name>", methods=['POST'])
def postPlayer(owner_name,player_name):
    for g in games:
        if g.owner_name == owner_name:
            game = g
    
    for person in game.players:
        if person.name == player_name:
            response = make_response()
            response.status_code = 400
            print("Attempted to add duplicate player names {}".format(player_name))
            return response
    new_player = player(player_name,None,None,len(game.players) + 1)


    game.players.append(new_player)

    

    
    
    
    return make_response(jsonify(todict(new_player)))
##@app.route("/games/<owner_name>/players/<player_name>/get_answers")
##def getAnswers(owner_name,player_name):
    ##return make_response(jsonify(todict(game.answers)))


@app.route("/games/<owner_name>/players/<player_name>/vote", methods=['POST'])
def postVotes(owner_name,player_name):
    content = request.get_json()
    answer_id = content['answer_id']
    
    for g in games:
        if g.owner_name == owner_name:
            game = g
    
    for person in game.players:
        if person.name == player_name:
            person.vote = answer_id
            game.turn.votes.append(person.vote)

    
    return make_response()

##@app.route("/games/<owner_name>/players/<player_name>/get_votes")
##def getVotes(owner_name,player_name):
    ##return make_response(jsonify(todict(game.votes)))

@app.route("/games/<owner_name>/players")
def getPlayers(owner_name):
    for g in games:
        if g.owner_name == owner_name:
            game = g
    return make_response(jsonify(todict(game.players)))

@app.route("/games/<owner_name>")
def getGame(owner_name):
    for g in games:
        if g.owner_name == owner_name:
            game = g
    return make_response(jsonify(todict(game)))

""" @app.route("/games/<owner_name>/get_points")
def getPoints(owner_name): """
