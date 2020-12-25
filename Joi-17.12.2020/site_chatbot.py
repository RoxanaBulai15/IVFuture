from flask import Flask, render_template
from chatbot import ChatBot


app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
   
   
if __name__ == '__main__':
   userAnswer = input("User: ")
   chat = ChatBot(userAnswer)
   chat.printForSiteMethod()

   app.run()
