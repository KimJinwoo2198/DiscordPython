import disnake
from disnake.ext import commands

bot = commands.Bot("!")

@bot.slash_command(
    name="슬래쉬 커맨드",
    description="간단한 예제",
    options=[
        disnake.Option("문자열", description="문자열", required=True),
        disnake.Option(
            "채널", description="채널", type=disnake.OptionType.channel
        ),
        disnake.Option(
            "숫자", description="숫자", type=disnake.OptionType.integer
        ),
    ],
)
async def command(inter, string, channel=None, number=1):
    channel = channel or inter.channel
    await inter.response.send_message(
        f"Sending {string} {number}x to {channel.mention}", ephemeral=True
    )
    await channel.send(string * number)