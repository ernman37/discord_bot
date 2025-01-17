import discord

from Client import Client
from Config import Config

config = Config()
client: Client = config.get_bot()


@client.tree.command(name="test", description='Test Reply', guild=config.get_guild_id())
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("Hello World!")

client.run(config.get_discord_token())
