# testBot by "The MAGA Manifesto"

import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
	print ("ready when you are")
	print ("I am running on " + bot.user.name)
	print ("With the ID " + bot.user.id)


@bot.command(pass_context = True)
async def wdt(ctx):
	await bot.say(":joy: who did this :joy:")
	print("user has pinged")

@bot.command(pass_context = True)
async def info(ctx, user: discord.Member):
	print("info is asked")
	# print info about user (name, ID, status and joined at)
	await bot.say("The user name is: {} \n".format(user.name) + "The user ID is: {} \n".format(user.id) + "The user status is: {} \n".format(user.status) + "The user joined at: {}".format(user.joined_at))

@bot.command(pass_context = True)
async def channels(ctx):
	print("called emojis command")
	for ch in bot.get_all_channels():
		await bot.say("%s " %(ch))


bot.run("Mzk0NDc3Mjk0NzkxNDI2MDUw.DSFA_g.9BDWVYZL9pUc6VJ8YeE2Qgh1wZY")