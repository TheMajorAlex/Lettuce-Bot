var Discord = require("discord.io");
var auth = require("./auth.json");


var bot = new Discord.Client({
	token: auth.token,
	autorun: true
});

console.log(bot);

console.log(auth.token);

bot.on("ready", function(e) {
	console.log("CONNECTED!");
	console.log("Logged in as: ");
	console.log(bot.username + ' - (' + bot.id + ')');
});

bot.on("message", function(user, userID, channelID, message, e) {
	bot.sendMessage({
		to: channelID,
		message: "Shut the fuck up plz"
	});
});

console.log("shit");