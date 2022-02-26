import nextcord
from nextcord.ext import commands

TESTING_GUILD_ID = 987654321 # 테스트 서버 ID


class CogExample(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[TESTING_GUILD_ID], description="테스트 커맨드")
    async def slash_command(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("This is a slash command in a cog!")

    @nextcord.user_command(guild_ids=[TESTING_GUILD_ID])
    async def user_command(self, interaction: nextcord.Interaction, member: nextcord.Member):
        await interaction.response.send_message(f"Hello, {member}!")

    @nextcord.message_command(guild_ids=[TESTING_GUILD_ID])
    async def message_command(self, interaction: nextcord.Interaction, message: nextcord.Message):
        await interaction.response.send_message(f"{message}")


def setup(bot):
    bot.add_cog(CogExample(bot))