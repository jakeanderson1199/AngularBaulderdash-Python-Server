##user_input = input("What is your name?")
class player:
    def __init__(self,name,points,answer,player_id):
        self.name = name
        self.points = points
        self.answer = answer
        self.id = player_id
    def __repr__(self):
        return "Name: {}, Points: {}, Answer: {}, ID: {}".format(self.name,self.points,self.answer,self.id)

p = player(0,0,0,0)
