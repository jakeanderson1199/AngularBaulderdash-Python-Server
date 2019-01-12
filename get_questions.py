class Get_questions:
    def get_questions(self):
        qlist = []
        with open("questions.txt") as f:
            for line in f:
                new = line.split(",")
                q = question(new[0].strip(),new[1].strip(),new[2].strip())
                qlist.append(q)
        return qlist