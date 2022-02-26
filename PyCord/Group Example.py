import discord

bot = discord.Bot()
TESTING_GUILD_ID = 987654321 # 테스트 서버 ID

math = bot.create_group("math", "Commands related to mathematics.")


@math.command(guild_ids=[TESTING_GUILD_ID])
async def add(ctx, num1: int, num2: int):
    await ctx.respond(f"**{num1}** + **{num2}** = **{num1+num2}**")

from discord.commands import SlashCommandGroup

math = SlashCommandGroup("수학", "커맨드는 수학에 의존한다.")


@math.command(guild_ids=[TESTING_GUILD_ID])
async def add(ctx, num1: int, num2: int):
    ...


bot.add_application_command(math)

bot.run("TOKEN")