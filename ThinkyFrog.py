# ThinkyFrog bot by "The MAGA Manifesto"

import discord
import random
import datetime
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix = '!')

#

@bot.event
async def on_ready():
	print("Loaded and ready at: " + str(datetime.now().time()))
	print("Logged into Discord as '{0.user.name}' ({0.user.id})\n".format(bot))

@bot.command(pass_context = True)
async def ping(ctx):
	await bot.say("{0.message.author.mention} :joy: :point_right: :ok_hand: :question:".format(ctx))
	print("user '{0.message.author}' has pinged at: ".format(ctx) + str(datetime.now().time()))

@bot.command(pass_context = True)
async def elo(ctx):
	elo = random.randint(1, 5000)
	emoji = None

	if elo < 1500:
		emoji = ":hyplul:"
	elif elo < 2000:
		emoji = ":feels:"
	elif elo < 2500:
		emoji = ":monkas:"
	elif elo < 3000:
		emoji = ":kkona:"
	elif elo < 3500:
		emoji = ":ok_hand:"
	elif elo < 4000:
		emoji = ":gasm:"
	elif elo >= 4000:
		emoji = ":eggplant: :sweat_drops: :weary:"

	await bot.say("Your elo is: {0} {1}".format(elo, emoji))

@bot.command(pass_context = True)
async def mcs(ctx):
	await bot.say(("{%d}" %random.randint(0,1)).format("yes", "no"))

@bot.command(pass_context = True)
async def pepo(ctx):
	await bot.say("here's a pepo for you ( ° ͜ʖ͡°)╭∩╮")

#vote 


@bot.command(pass_context = True)
async def commands(ctx):
	embed = discord.Embed(title = "Commands", description = "you can use the following commands: ", color = 0x073097)
	embed.set_footer(text = "this is a bot by 'The MAGA Manifesto#6565'")
	embed.add_field(name = "!ping", value = "pings at the bot, expecting a response (used to check the bot's status)", inline = True)
	embed.add_field(name = "!elo", value = "displays your OverWatch Skill Rating", inline = True)
	embed.add_field(name = "!mcs", value = "'magic conch shell' answers your question with 'yes' or 'no'", inline = True)
	embed.add_field(name = "!vote", value = "opens a vote for 15 seconds, vote with 'voteYes' or 'voteNo'", inline = True)
	embed.set_thumbnail(url = bot.user.avatar_url)

	await bot.say(embed = embed)


bot.run("Mzk0NTA1Mjg2MjgwNDEzMTg1.DSFmGw.oF-2UTMrJYqrk3GMTl48J8t4DYc")