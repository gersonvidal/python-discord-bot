import discord 
import os
from discord.ext import commands 

# Get Discord Key
key = os.getenv('DISCORD_KEY')

# Configure intents
intents = discord.Intents.default()  # Enable basic intents
intents.message_content = True  # Enable message content intent

# Initialize bot 
bot = commands.Bot(command_prefix = '$', intents = intents)

@bot.command()
async def salute(context):
    await context.send('Hola soy un bot caramelito del fortnite')
    
bot.run(key)