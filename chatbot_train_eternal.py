from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

chatterbot = ChatBot("Training Example")
chatterbot.set_trainer(ListTrainer)

conv = open('ESOTSM.srt', 'r').readlines()

chatterbot.set_trainer(ListTrainer)
chatterbot.train(conv)