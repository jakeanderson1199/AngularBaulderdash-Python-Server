from random import randint

class Answer:
    def __init__(self,player_id):
        self.answer_id = randint(20,100000)
        self.player_id = player_id
        self.text = 0
    def __repr__(self):
        return "Player ID: {}, Answer ID: {}, Answer: {}".format(self.player_id,self.answer_id, self.text)