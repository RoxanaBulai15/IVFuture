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
            for p in self.data['chatbot']:
                gasit = 0
                tagg = 'noanswer'

                if p['tag'] != 'noanswer':
                    for i in p['patterns']:
                        if i == self.userAnswer:
                            gasit = 1
                            tagg = p['tag']
                        if gasit == 1:
                            break
                else:
                    print("ChatBot: " + random.choice(p['responses']))
                    self.userAnswer = input("User: ")

                if tagg == 'greeting':
                    print("ChatBot: " + random.choice(p['responses']))
                    self.userAnswer = input("User: ")
                elif tagg == 'good':
                    print("ChatBot: " + random.choice(p['responses']))
                    ok = 1
                #elif tagg == 'noanswer':
                #    print(p['tag'])
                #    print("ChatBot: " + random.choice(p['responses']))
                    #print('aaaaaaa')
                    #for j in p['tag']:
                     #   print(j)
                      #  break
                       # if j == tagg:
                        #    print("ChatBot: " + random.choice(p['responses']))
                         #   break


if __name__ == '__main__':
    userAnswer = input("User: ")
    chatBot = ChatBot(userAnswer)
    chatBot.check_answer()

