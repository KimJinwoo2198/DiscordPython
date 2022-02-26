import datetime
import discord

bot = discord.Bot()

@bot.command()
async def timeout(ctx, member: discord.Member, minutes: int):
    duration = datetime.timedelta(minutes=minutes)
    await member.timeout_for(duration)
    await ctx.reply(f"해당 멤버를 {minutes}분 동안 TimeOut 시켰어요!")

bot.run("TOKEN")