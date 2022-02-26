import discord
from discord.commands import Option

bot = discord.Bot()
TESTING_GUILD_ID = 987654321 # 테스트 서버 ID

@bot.slash_command(guild_ids=[TESTING_GUILD_ID])
async def hello(
    ctx: discord.ApplicationContext,
    name: Option(str, "이름을 입력해주세요."),
    gender: Option(str, "성별을 골라주세요 !", choices=["여자", "남자", "둘다 아님"]),
    age: Option(int, "나이를 입력해주세요. ", min_value=1, max_value=99, default=18)
):
    await ctx.respond(f"안녕하세요 {name}님. 당신의 성별은 {gender}이시고, 나이는 {age}세 이시군요.")


@bot.slash_command(guild_ids=[TESTING_GUILD_ID])
async def channel(
    ctx: discord.ApplicationContext,
    channel: Option([discord.TextChannel, discord.VoiceChannel], "채널을 선택해주세요.")
):
    await ctx.respond(f"안녕하세요. 당신은 {channel.mention}채널을 선택하셨습니다.")


@bot.slash_command(name="파일")
async def say(
    ctx: discord.ApplicationContext,
    attachment: Option(
        discord.Attachment,
        required=False,
    ),
):
    file = await attachment.to_file()
    await ctx.respond("당신의 파일입니다.", file=file)


bot.run("TOKEN")