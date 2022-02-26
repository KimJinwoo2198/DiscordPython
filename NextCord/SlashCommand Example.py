import nextcord
from nextcord import Interaction, SlashOption

TESTING_GUILD_ID = 987654321  # 테스트 서버 ID

client = nextcord.Client()

@client.slash_command(guild_ids=[TESTING_GUILD_ID], description="Ping command")
async def ping(interaction: Interaction):
    await interaction.response.send_message("Pong!")
    
client.run("token")