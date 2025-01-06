import discord 
from discord.ext import commands 
import random
import os
from services.fortnite_api_io import FortniteApiIo

# Get Discord Key
key = os.getenv('DISCORD_KEY')

# Initialize Fornite API
fortnite = FortniteApiIo()

# Initialize info that isn't changing soon
current_locations = fortnite.get_list_of_current_pois()
current_loot = fortnite.get_list_of_current_loot()

# Configure intents 
intents = discord.Intents.default() # Enable basic intents 
intents.message_content = True # Enable message content intent

# Initialize bot 
bot = commands.Bot(command_prefix = '$', intents = intents)

@bot.command()
async def salute(context):
    await context.send('Hola soy un bot caramelito del fortnite')
    
@bot.command() 
async def loot(context):
    # Copy the array so we can delete chosen objects and don't give duplicates
    aux_loot = current_loot.copy()
    
    embed = discord.Embed(
        title = f"El loot para {context.author.name}",
        description = "La bola mágica ha decidido tu siguiente loot",
        color = discord.Color.red()
    )
    
    # Choose random loadout for the user 
    # 6 is excluded, mening we only go from 1 to 5
    for i in range(1, 6):
        # Choose a random item from the loot list
        chosen_index = random.randrange(len(aux_loot))
        item_name = aux_loot.pop(chosen_index) # Deletes the item from the list and returns it to us
        
        # inline = False helps us make every item have its own line 
        embed.add_field(name = f"Item {i}",
                        value = f"{item_name}",
                        inline = False)
        
    embed.set_thumbnail(url = f"{context.author.avatar.url}")
    
    await context.send(embed = embed)
        
@bot.command()
async def drop(context):
    embed = discord.Embed(
        title = "La ubicación para caer será...",
        description = "La bola mágica ha decidido dónde vamos a regalar nuestro loot...",
        color = discord.Color.blue()
    )
    
    # Choose a random location for the user
    random_location = random.choice(current_locations)
    
    embed.add_field(name = "Ubicación", 
                    value = f"{random_location}")
    
    await context.send(embed = embed)
        
bot.run(key)