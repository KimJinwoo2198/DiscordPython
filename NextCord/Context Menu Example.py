import nextcord

TESTING_GUILD_ID = 987654321  # 테스트 서버 ID

client = nextcord.Client()


@client.user_command(guild_ids=[TESTING_GUILD_ID])
async def member_info(interaction: nextcord.Interaction, member: nextcord.Member):
    await interaction.response.send_message(f"Member: {member}")


@client.message_command(guild_ids=[TESTING_GUILD_ID])
async def my_message_command(interaction: nextcord.Interaction, message: nextcord.Message):
    await interaction.response.send_message(f"Message: {message}")


client.run("token")