import discord

from Chatter import Chatter

class Client(discord.Client):
    def __init__(self, *, intents: discord.Intents, command_prefix: str = '/', guild_id: discord.Object, chatter: Chatter):
        super().__init__(intents=intents, command_prefix=command_prefix)
        self.tree = discord.app_commands.CommandTree(self)
        self.guild_id = guild_id
        self.chatter = chatter

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            synced = await self.tree.sync(guild=self.guild_id)
            print(f"Synced {len(synced)} commands to guild")
        except Exception as e:
            print(e)

    async def on_message(self, message: discord.Message):
        print(f'Message from {message.author}: {message.content}')
        if self.user.mentioned_in(message):
            response = self.chatter.ask(message.content)
            print(response)
            await message.channel.send(response)
