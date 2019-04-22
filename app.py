from flask import Flask,render_template,jsonify, make_response,json,request, send_from_directory
from datetime import datetime
import re
from game_class import *
from player_class import *
from to_dict import *
from Answer_class import Answer
from flask_cors import CORS

app = Flask(__name__, static_url_path='')

CORS(app)



@app.route("/")
def home():
    return send_from_directory('client', 'index.html')

#####  Uncomment when running prod angular app
#@app.route('/<path>')
#def send_js(path):
#    return send_from_directory('client', path)




@app.route("/api/games/<owner_name>", methods=['POST'])
def postGame(owner_name):
    ##global game
    game = Game()
    
    game.owner_name = owner_name
    game.new_turn()
    games.append(game)
    content = todict(game)
    print(game.owner_name)
    return make_response(jsonify(content))
    
@app.route("/api/games")
def getGames():
    ##games = []
    ##games.append(game) 

    return make_response(jsonify(todict(games)))


@app.route("/api/games/<owner_name>/players/<player_name>/answer", methods=['POST'])
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


@app.route("/api/games/<owner_name>/players/<player_name>", methods=['POST'])
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
    new_player = player(player_name,0,None,len(game.players) + 1)


    game.players.append(new_player)

    

    
    
    
    return make_response(jsonify(todict(new_player)))
##@app.route("/games/<owner_name>/players/<player_name>/get_answers")
##def getAnswers(owner_name,player_name):
    ##return make_response(jsonify(todict(game.answers)))


@app.route("/api/games/<owner_name>/players/<player_name>/vote", methods=['POST'])
def postVotes(owner_name,player_name):
    content = request.get_json()
    answer_id = content['vote']
    
    for g in games:
        if g.owner_name == owner_name:
            game = g
    
    for person in game.players:
        if person.name == player_name:
            person.vote = answer_id
            game.turn.votes.append(person.vote)
    for person in game.players:
        if person.vote['answer'] == game.turn.current_question.real_answer: ##TODO somehow change person.vote.answer so that it gets the text of the persons answer//Need to transfer the game class "votes" into the server so that you can access it to assign points.
            person.points += 2
        for vote in game.turn.votes:
            if person.answer.text == vote['answer']:
                person.points += 1

    
    return make_response(jsonify(todict(game)))

##@app.route("/games/<owner_name>/players/<player_name>/get_votes")
##def getVotes(owner_name,player_name):
    ##return make_response(jsonify(todict(game.votes)))

@app.route("/api/games/<owner_name>/players")
def getPlayers(owner_name):
    for g in games:
        if g.owner_name == owner_name:
            game = g
    return make_response(jsonify(todict(game.players)))

@app.route("/api/games/<owner_name>")
def getGame(owner_name):
    for g in games:
        if g.owner_name == owner_name:
            game = g
    return make_response(jsonify(todict(game)))

""" @app.route("/games/<owner_name>/get_points")
def getPoints(owner_name): """

@app.route("/api/games/<owner_name>/turns", methods=['POST'])
def nextTurn(owner_name):
    for g in games:
        if g.owner_name == owner_name:
            game = g
    game.new_turn()
    return make_response(jsonify(todict(game)))
