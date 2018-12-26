from flask import Flask, request, json, jsonify, make_response
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content


@app.route("/games")
def getGame():
    
    content = todict(game)
   
    return make_response(jsonify(content))

@app.route("/players")
def getPlayer():
    
    player = Player('jake')

    content = todict(player)

    return jsonify(content)

@app.route("/players", methods=['POST'])
def postPlayer():
    
    content = request.get_json()
    
    nm =  content['name']
    addr = content['address']
    city = addr['city']

    

    player = Player(nm)

    player.name = nm

    player.address.city = city

    game.player = player

    print(nm)
    
    
    return make_response(jsonify(content))

def todict(obj, classkey=None):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = todict(v, classkey)
        return data
    elif hasattr(obj, "_ast"):
        return todict(obj._ast())
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [todict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key, todict(value, classkey)) 
            for key, value in obj.__dict__.items() 
            if not callable(value) and not key.startswith('_')])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj
    
class Player:
  
  def __init__(self, name):
    self.name = name
    self.address = Address('mpls')
    #self.dic = self.__dict__

class Address:
  def __init__(self, city):
    self.city = city


class Game:
    def __init__(self):
        self.player = Player('jake')

    def changePlayer(self, player): 
        self.player = player

game = Game()