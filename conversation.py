import re, math
from random import randint
from cosine_similarity import CosineSimilarity

class Conversation:

    def __init__(self):
        self.intentions = []
        self.current_intention = None

    def insert_intention(self, intention):
        self.intentions.append(intention)

    def get_response(self, question, no_responses):

        responses = []
        action = """"""
        similarity_before = 0.2

        cosine_similarity = CosineSimilarity()
        
        if not self.current_intention:
            for intention in self.intentions:
                for dialog in intention.get_dialogs():
                    for defined_question in dialog.get_questions():
                        similarity = cosine_similarity.compare(defined_question, question)
                        if similarity > similarity_before:
                            similarity_before = similarity
                            self.current_intention = intention
                            responses = dialog.get_responses()
                            action = dialog.get_action()
        else:
            for dialog in self.current_intention.get_dialogs():
                for defined_question in dialog.get_questions():
                    similarity = cosine_similarity.compare(defined_question, question)
                    if similarity > similarity_before:
                        similarity_before = similarity
                        responses = dialog.get_responses()
                        action = dialog.get_action()
                    
        if action:
            exec(action.replace("INPUT", "\"" + question + "\""))
        if len(responses) > 0:
            if type(responses) == str:
                return responses
            return responses[randint(0,len(responses)-1)]
        else:
            if not self.current_intention:
                return no_responses[randint(0,len(no_responses)-1)]
            else:
                self.current_intention = None
                return self.get_response(question)
        