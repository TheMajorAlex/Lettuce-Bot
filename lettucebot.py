# Import the discord library
# First, you have to download it by typing python -m pip install discord.py[voice] into the command prompt
import discord
from discord.ext.commands import Bot
from discord.ext import commands

# For logging errors
import logging
logging.basicConfig(level=logging.INFO)

# Creates the client
Client = discord.Client()

# Creates a bot that uses the defined bot prefix below
bot_prefix = "::"
client = commands.Bot(command_prefix=bot_prefix)

#Fires whent the bot is online
@client.event
async def on_ready():
	print("Bot is online!")
	print("Name: ()".format(client.user.name))
	print("ID: ()".format(client.user.id))


# You can add as many commands as you want to this
# Just type @client.command(pass_context=True) above it
# The function name will be the command the user has to type 
# "await client.say()" Will have the bot say something
# The await keyword basically means wait until client.say is sucesfully ran to do anything else 

@client.command(pass_context=True)
async def ping(ctx):
	await client.say("Pong!")

@client.command(pass_context=True)
async def shit(ctx):
	await client.say("I took a massive shit :poop:")

# Do not let anybody who's untrusted get this token
# They can fuck up our fucking shit
client.run("Mzc1NzA3MDk1MDE1NzUxNjgw.DNzwUw._8N94XWJqxUDezjW1mXqOwexKeQ")
