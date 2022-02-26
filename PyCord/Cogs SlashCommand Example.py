from discord.commands import slash_command
from discord.ext import commands

TESTING_GUILD_ID = 987654321 # 테스트 서버 ID

class CogsExample(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[TESTING_GUILD_ID])
    async def hello(self, ctx):
        await ctx.respond("안녕하세요 !")

    @slash_command()
    async def hi(self, ctx):
        await ctx.respond("안녕하세요 !")


def setup(bot):
    bot.add_cog(CogsExample(bot))