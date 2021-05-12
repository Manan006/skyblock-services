from dotenv import load_dotenv
import discord
import os
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client()
@bot.event
async def on_ready():
    print("ready")

@bot.event
async def on_message(ctx):
    print(ctx)


bot.run(TOKEN)