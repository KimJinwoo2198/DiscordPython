import nextcord

TESTING_GUILD_ID = 987654321  # 테스트 서버 ID

client = nextcord.Client()


@client.slash_command(guild_ids=[TESTING_GUILD_ID], description="main command")
async def main(interaction: nextcord.Interaction):
    pass


@main.subcommand(description="서브커맨드 1")
async def sub1(interaction: nextcord.Interaction):
    await interaction.response.send_message("서브 커맨드 예시 1!")


@main.subcommand(description="서브커맨드 2")
async def sub2(interaction: nextcord.Interaction):
    await interaction.response.send_message("서브 커맨드 예시 2!")


@main.subcommand(description="그룹 서브커맨드")
async def main_group(interaction: nextcord.Interaction):
    pass


@main_group.subcommand(description="서브커맨드 그룹 서브커맨드 1")
async def subsub1(interaction: nextcord.Interaction):
    await interaction.response.send_message("서브커맨드 그룹 서브커맨드 1!")


@main_group.subcommand(description="서브커맨드 그룹 서브커맨드 2")
async def subsub2(interaction: nextcord.Interaction):
    await interaction.response.send_message("서브커맨드 그룹 서브커맨드 2!")


client.run("token")