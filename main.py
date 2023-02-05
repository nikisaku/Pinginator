import discord
import os
import pytz

from datetime import datetime as dt
from dotenv import load_dotenv

load_dotenv()
timezone = pytz.timezone('Europe/Warsaw')
CURRENT_TIME = dt.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        @client.event
        async def on_message(message):
            if client.user.mentioned_in(message):
                await message.channel.send(f'{message.author.mention} https://www.youtube.com/watch?v=fPq60AoPPlo')
                print(f'{CURRENT_TIME} - Pinged {message.author.name} in the server {message.guild.name} for a message in the #{message.channel.name}')
                 


client = MyClient(intents=discord.Intents.default())
client.run(TOKEN)
