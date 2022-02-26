import discord

bot = discord.Bot()
TESTING_GUILD_ID = 987654321 # 테스트 서버 ID

@bot.slash_command(guild_ids=[TESTING_GUILD_ID])
async def hello(ctx):
    await ctx.respond(f"Hello {ctx.author}!")


@bot.slash_command(name="hi")
async def global_command(ctx, num: int):
    await ctx.respond(f"{num}!")


@bot.slash_command(guild_ids=[TESTING_GUILD_ID])
async def joined(ctx, member: discord.Member = None):
    user = member or ctx.author
    await ctx.respond(f"{user.name} 님이 {discord.utils.format_dt(user.joined_at)}에 입장하셨어요.")


bot.run("TOKEN")