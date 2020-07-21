class Dialog:

    def __init__(self, questions, responses, action):
        self.responses = responses
        self.questions = questions
        self.action = action

    def get_responses(self):
        return self.responses

    def get_questions(self):
        return self.questions

    def get_action(self):
        return self.action