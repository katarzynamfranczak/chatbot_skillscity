

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import sys

bot = ChatBot('My_Bot')

def train(bot, training_data_path):
	path = training_data_path
	trainer = ListTrainer(bot)
	for file in os.listdir(path):
		data = open(path + file, 'r').readlines()
		trainer.train(data)

def main():
	args = sys.argv[1:]

	# if we have an argument in the form of --train path/to/training/data
	# then we train the bot
	if len(args) == 2 and args[0] == '--train':
		training_data_path = args[1]
		print("Training Bot on input data provided")
		train(bot, training_data_path)
		print("Bot Training Completed")
	exit_conditions = (":q", "quit", "exit", "bye", "goodbye")
	while True:
		input_message = input('>: ')
		if input_message.lower().strip() not in exit_conditions:
			result = bot.get_response(input_message)                        
			reply = str(result)
			print(reply)
		else:
			print('Bye')
			break


if __name__ == '__main__':
	main()