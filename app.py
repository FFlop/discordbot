import os
import discord
from discord.ext import commands
from dotenv import  load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix = "n!n")
client_id = os.getenv("CLIENT_ID")
guild_id = os.getenv("GUILD_ID")
 
@commands.is_owner()
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs{extension}')

@commands.is_owner()
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs{extension}')

@commands.is_owner()
@bot.command()
async def reload(ctx, extensions):
    bot.unload_extension(f'cogs{extension}')
    bot.load_extension(f'cogs{extension}')

if __name__ == "__main__":        
    for filename in os.listdir("/home/andrew/Documents/discordbot1/bot/cogs"):
        if filename.endswith(".py"):
                bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(client_id)