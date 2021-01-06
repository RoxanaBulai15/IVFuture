import json
import random

import wikipedia


class ChatBot:
    def __init__(self, userAnswer):
        self.userAnswer = userAnswer
        with open('chatbot.json') as json_file:
            self.data = json.load(json_file)

    def check_answer(self):

        while True:
            for p in self.data['chatbot']:
                if p['tag'] != 'noanswer':
                    for i in p['patterns']:
                        if i == self.userAnswer:
                            return random.choice(p['responses'])

                else:
                    answer=self.userAnswer
                    message = "Sorry that I didn't help you, choose another game from the list. "
                    if self.userAnswer == "Yes":
                        return wikipedia.summary(answer, sentences=2)
                    elif self.userAnswer == "No":
                        print('a')
                        return message
                    return random.choice(p['responses'])

    def printForSiteMethod(self):
        print('Am facut o instanta dintr-un fisier in altul')

    def wikipediaSearch(self, answer):
        message = "Sorry that I didn't help you, choose another game from the list. "
        if self.userAnswer == "Yes":
            return wikipedia.summary(answer, sentences=2)
        if self.userAnswer == "No":
            print('a')
            return message
