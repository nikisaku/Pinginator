import discord

TOKEN = 'your_discord_bot_token'


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


client = MyClient()
client.run(TOKEN)
