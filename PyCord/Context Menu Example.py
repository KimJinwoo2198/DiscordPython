import discord

bot = discord.Bot()
TESTING_GUILD_ID = 987654321 # 테스트 서버 ID

@bot.user_command(guild_ids=[TESTING_GUILD_ID])
async def mention(ctx, member: discord.Member):
    await ctx.respond(f"{ctx.author.name}님! {member.mention}님을 맨션했어요!")


@bot.message_command(name="ID")
async def show_id(ctx, message: discord.Message):
    await ctx.respond(f"{ctx.author.name}님! 여기 아이디예요\n 아이디:{message.id}")


bot.run("TOKEN")