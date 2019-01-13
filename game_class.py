from question_class import *
from player_class import *
from turn_class import Turn


class Game:
    def __init__(self):
        self.question_list = self.get_questions()
        self.start = False
        self.players = []
        self.owner_name = None
        self.index = 0
        


    def get_questions(self):
        qlist = []
        with open("questions.txt") as f:
            for line in f:
                new = line.split(",")
                q = Question(new[0].strip(),new[1].strip(),new[2].strip())
                qlist.append(q)
        return qlist
    def new_turn(self):
        self.index += 1
        self.turn = Turn(self.question_list[self.index])
games = []
