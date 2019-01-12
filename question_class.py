class Question:
    def __init__(self,question,category,real_answer):
        self.question = question
        self.category = category
        self.real_answer = real_answer
    def __repr__(self):
        return "Question: {}\n Category: {}\n Answer: {}\n".format(self.question,self.category,self.real_answer)
    def __str__(self):
        return "{},{},{}".format(self.question,self.category,self.real_answer)




qlist = []
with open("questions.txt") as f:
    for line in f:
        new = line.split(",")
        q = Question(new[0].strip(),new[1].strip(),new[2].strip())
        qlist.append(q)

