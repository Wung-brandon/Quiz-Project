class Question:
    def __init__(self,text,question):
        self.q_text = text
        self.q_question = question

new_q = Question("wung", "brandon")
print(new_q.q_text)