from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from memes import prequel_quotes as memes

app = Flask(__name__)

chatbot = ChatBot("R2bot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ListTrainer(chatbot)
trainer.train(memes)

@app.route("/bot")
def home():
    return render_template("home.html")

@route('/', method='GET')
def new_chat()
    user_message = requests.args.get('message')
    return str(chatbot.get_response(user_message))


if __name__ == "__main__":
    app.run()