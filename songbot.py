import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from get_spotify_title import get_spotify_window_title, get_current_song

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    announce_song.start()

@tasks.loop(seconds=10)
async def announce_song():
    last_announced = None
    channel_id = 1085525133160103977  # Replace with your desired channel ID

    while True:
        title = get_spotify_window_title()
        if title != "No title found":
            artist, name = get_current_song(title)
            current_song = f"{artist} - {name}"

            if current_song != last_announced:
                channel = bot.get_channel(channel_id)
                await channel.send(f"🎶 Now playing: **{current_song}**")
                last_announced = current_song

if __name__ == "__main__":
    bot.run(TOKEN)
