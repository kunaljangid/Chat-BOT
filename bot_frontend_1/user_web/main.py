from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot = ChatBot('Test')
# bot = ChatterBotCorpusTrainer(bott)

# conv = open('chats.txt','r').readlines().split()
# bot.set_trainer(ListTrainer)
trainer = ListTrainer(bot)
# bot.train(conv)
trainer.train([
    "Hi there!",
    "Hello",
])
trainer.train([
    "how are you",
    "i am good, how are you",
    "i am good, how are you",
    "it is windy outside",
    "yes it is really windy",
])


#######################################################################
app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/process' , methods=['POST'])
def process():
    user_input = request.form['user_input']
    bot_response = bot.get_response(user_input)
    bot_response = str(bot_response)
    print("friend " + bot_response)
    return render_template('index.html',user_input=user_input,bot_response=bot_response)

if __name__=='__main__':
    app.run(debug=True , port = 5002)
