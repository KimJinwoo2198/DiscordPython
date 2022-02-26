import discord
from discord.ext import commands

intents = discord.Intents(guilds=True,members=True,messages=True)

bot = commands.Bot(
    command_prefix="!",
    description="유저 정보를 보여주는 예시입니다.",
    intents=intents,
)

@bot.slash_command(name="유저정보", description="유저정보를 얻을 수 있습니다.")
async def info(ctx, user: discord.Member = None):
    user = user or ctx.author
    e = discord.Embed()
    e.set_author(name=user.name)
    e.add_field(name="ID", value=user.id, inline=False)
    e.add_field(
        name="서버 접속일",
        value=discord.utils.format_dt(round(user.joined_at.timestamp()), "F"),
        inline=False,
    )
    e.add_field(
        name="계정 생성일",
        value=discord.utils.format_dt(round(user.created_at.timestamp()), "F"),
        inline=False,
    )
    colour = user.colour
    if colour.value:
        e.colour = colour

    if isinstance(user, discord.User):
        e.set_footer(text="이 사람은 해당 서버에 존재하지 않습니다.")

    await ctx.respond(embed=e)


bot.run("your token")