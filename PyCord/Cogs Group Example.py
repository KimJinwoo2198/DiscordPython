import discord
from discord.commands import CommandPermission, SlashCommandGroup
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    greetings = SlashCommandGroup("Hello", "Hi")

    international_greetings = greetings.create_subgroup("International", "International greetings")

    secret_greetings = SlashCommandGroup(
        "secret_greetings",
        "Secret greetings",
        permissions=[CommandPermission("owner", 2, True)],
    )

    @greetings.command()
    async def hello(self, ctx):
        await ctx.respond("Cogs 서브커맨드 예시입니다.")

    @international_greetings.command()
    async def aloha(self, ctx):
        await ctx.respond("안녕하세요, a Korean greeting")

    @secret_greetings.command()
    async def secret_handshake(self, ctx, member: discord.Member):
        await ctx.respond(f"{member.mention} I love you")


bot.add_cog(Example(bot))