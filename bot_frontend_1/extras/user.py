from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot = ChatBot('Friend')
 # create Chatbot

trainer = ListTrainer(bot) # training of the bot
# bot.set_trainer(ListTrainer)
for knowledge in os.listdir('base'):
    botmemory = open('base/'+knowledge,'r').readline()
    trainer.train(botmemory)
# bot = ChatBot(bot)
while True :
    user_input = input("Say hi to my friend: ")
    # bot_response = bot.get_latest_response(user_input)
    bot_response = trainer.get_response(user_input)
    bot_response = str(bot_response)
    print("friend " + bot_response)
