from flask import Flask, render_template
import chatbot as mymodule

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get')
def get_bot_response(userAnswer):
    chat = mymodule.ChatBot(userAnswer)
    return str(chat.check_answer())


if __name__ == '__main__':
    userAnswer = input("User: ")
    chat = mymodule.ChatBot(userAnswer)
    #chat.check_answer();
    #get_bot_response(chat)
    #chat.check_answer()
    chat.printForSiteMethod()

    app.run()
