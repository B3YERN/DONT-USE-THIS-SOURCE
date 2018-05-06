import discord
from discord.ext import commands
import asyncio
import random
import traceback
import logging
import os
import client
bot = commands.Bot (command_prefix = "!")
client = discord.Client()

        
bot.run(os.getenv('TOKEN'))
