import discord
from discord.ext import commands, tasks
import subprocess

import os
from dotenv import load_dotenv


intents = discord.Intents.all()


bot = discord.Bot( 
    intents=intents, 
    debug_guildes=["debug_guildes"]
)


player_name_var = None


@bot.event
async def on_ready():
    await bot.sync_commands()
    print(f'{bot.user.name} has connected to Discord!')

    await bot.change_presence(activity=discord.Activity(name="zu!", type=discord.ActivityType.watching, status=discord.Status.online)) # Status

# Bot herunterfahren
@bot.slash_command(description="fährt den bot herunter")
async def stop(ctx):
    await ctx.respond("Der Bot wird heruntergefahren.")
    print(f'{bot.user.name} has disconnected!')
    await bot.close()


@bot.slash_command(description='Führt das Quiz aus.')
async def wim(ctx, player_name_entry: str):
    global player_name_var
    player_name_var = player_name_entry  # Speichere den Spielername in der globalen Variable
    subprocess.Popen(['python', r'C:\Users\larsr\iCloudDrive\Python\Wissen-ist-Macht\Grafik.py'])
    await ctx.send('Das Quiz wurde gestartet!')
    print(f"Player Name: {player_name_var}")


load_dotenv()
bot.run(os.getenv("Token"))
