import disnake
from disnake.ext import commands

bot = commands.Bot(
    command_prefix="!",
    test_guilds=[987654321],
)

async def avatar(inter: disnake.ApplicationCommandInteraction, user: disnake.User):
    emb = disnake.Embed(title=f"{user}'s avatar")
    emb.set_image(url=user.display_avatar.url)
    await inter.response.send_message(embed=emb)

@bot.message_command(name="Reverse")
async def reverse(inter: disnake.ApplicationCommandInteraction, message: disnake.Message):
    await inter.response.send_message(message.content[::-1])

bot.run("TOKEN")