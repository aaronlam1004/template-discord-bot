/*
 * Getting started:
 * 	Basic tutorial: https://www.digitalocean.com/community/tutorials/how-to-build-a-discord-bot-with-node-js
 *
 * Discord.JS Resources:
 * 	Discord.JS API: https://discord.js.org/#/docs/main/stable/general/welcome
 *
 * Discord Resources:
 * 	Discord API: https://discord.com/developers/docs/intro
 * 	Markdowns to Discord: https://support.discord.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline-
 *
 * Other Resources:
 * 	Source code of AL|CE bot used on UCI ICS Discord (really cool bot, made in Java, actually uses official API calls)
 * 		-> https://github.com/Auxiliatrix/ALICE 
 */

// Import the Discord.JS library
const Discord = require("discord.js");

// Create new client to connect to Discord server
const bot = new Discord.Client();

// Read the config file to use
const config = require("./config.json");

// Print this statement when bot is ready
bot.on("ready", () => {
	console.log("The bot started!!!");
});

// Do something when a message is sent
bot.on("message", message => {

	var content = message.content.split(/ +/); // Splits message by spaces (@user hello -> [user, hello])

	// user: ping
	// bot: @user, pong
	if (message.content.toLowerCase() == "ping") {
		message.reply("pong");
	}
	
	// Messages that mention the bot 
	else if (content[0] === "<@!" + bot.user.id + ">") {

		if (content[1] != null) {

			switch(content[1].toLowerCase()) {

				// user: @bot hi
				case "hi": 
					message.reply("This is a template Discord bot using NodeJS and Discord.JS.");
					break;

				// user: @bot doc
				case "doc":
					message.reply(config.documentation);
					break;
			}
		}
	}
});

// Bot login 
bot.login(config.token);

// Alternatively could use,
//bot.login("YOUR BOT TOKEN HERE")
