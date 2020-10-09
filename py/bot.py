# Getting started:
# 	Basic tutorial: https://realpython.com/how-to-make-a-discord-bot-python/
# 
# discord.py Resources:
#  discord.py API: https://discordpy.readthedocs.io/en/latest/# 
# 
# Discord Resources:
# 	Discord API: https://discord.com/developers/docs/intro
# 	Markdowns to Discord: https://support.discord.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline-
# 
# Other Resources:
# 	Source code of AL|CE bot used on UCI ICS Discord (really cool bot, made in Java, actually uses official API calls)
# 		-> https://github.com/Auxiliatrix/ALICE 

import discord

import sys, io
from os import path

if __name__ == '__main__':

	bot = discord.Client()

	@bot.event
	async def on_ready():
		print("The bot started!!!")

	# Do something when a message is sent
	@bot.event
	async def on_message(message):
		
		# user: ping
		# bot: @user, pong
		if message.content == "ping":
			await message.channel.send(message.author.mention + ", " + "pong")

		# Checks if bot is mentioned
		bot_mention = str(bot.user.mention)[0:2] + "!" + str(bot.user.mention)[2:]

		# User mentions bot in message
		if message.content.startswith(bot_mention):

			# Checks if message is [@user, <arg>]
			if len(message.content.split(" ")) == 2:

				arg = message.content.split()[1]

				# user: @bot hi	
				if arg.lower() == "hi":
					await message.channel.send(message.author.mention + ", " + "This is a template Discord bot using Python and discord.py.")

				# user: @bot doc
				elif arg.lower() == "doc":
					text = ""
					with open("./doc.txt", "r") as docfile:
						text = docfile.read()
					await message.channel.send(message.author.mention + ", " + text)

	# Run the bot
	if path.isfile("./token.txt"):
		with open("token.txt", "r") as key:
			bot.run(key.read().rstrip("\n"))
	
	# Alternatively
	#bot.run("YOUR BOT TOKEN HERE")
