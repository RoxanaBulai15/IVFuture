import json


class ChatBot:
    def __init__(self, userAnswer):
        self.userAnswer = userAnswer
        with open('chatbot.json') as json_file:
            self.data = json.load(json_file)

    def check_answer(self):
        print("Here")
        while True:
            for p in self.data['chatbot']:
                for i in p['patterns']:
                    if i == self.userAnswer:
                        for j in p['responses']:
                            print("Chatbot: " + j)
                            break
            # if ok == 0:
            #     x = input("Chatbot: Invalid answer. Enter again: ")


if __name__ == '__main__':
    userAnswer = input("User: ")
    chatBot = ChatBot(userAnswer)
    chatBot.check_answer()
