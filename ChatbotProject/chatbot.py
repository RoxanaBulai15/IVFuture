import json
import random


class ChatBot:
    def __init__(self, userAnswer):
        self.userAnswer = userAnswer
        with open('chatbot.json') as json_file:
            self.data = json.load(json_file)

    def check_answer(self):
        ok = 0
        while ok == 0:
            gasit = 0
            for p in self.data['chatbot']:
                tagg = 'noanswer'
                if p['tag'] != 'noanswer':
                    for i in p['patterns']:
                        if i == self.userAnswer:
                            gasit = 1
                            tagg = p['tag']  # greeting or good
                            if tagg == 'greeting':
                                print("ChatBot: " + random.choice(p['responses']))
                                return random.choice(p['responses'])
                                self.userAnswer = input("User: ")
                            if tagg == 'good':
                                print("ChatBot: " + random.choice(p['responses']))
                                return random.choice(p['responses'])
                                ok = 1
                        if gasit == 1:
                            break
            if gasit == 0:
                print("ChatBot: " + random.choice(p['responses']))
                return random.choice(p['responses'])
                self.userAnswer = input("User: ")

    def printForSiteMethod(self):
        print('Am facut o instanta dintr-un fisier in altul')

    # if __name__ == '__main__':
    #     userAnswer = input("User: ")
    #     chatBot = ChatBot(userAnswer)
    #     chatBot.check_answer()