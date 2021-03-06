import json
import random

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
                    print("ChatBot: " + random.choice(p['responses']))
                    return random.choice(p['responses'])

    def printForSiteMethod(self):
        print('Am facut o instanta dintr-un fisier in altul')