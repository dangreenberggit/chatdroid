from flask import Flask, render_template, request
import random
from crap_memes import memes

app = Flask(__name__)


@route('/', method='GET')
def new_chat()
    user_message = requests.args.get('message')
    bot_message = random.choice(memes)
    return {"message": bot_message}

if __name__ == "__main__":
    app.run()