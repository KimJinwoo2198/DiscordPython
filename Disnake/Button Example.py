import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands

bot = commands.Bot(command_prefix="!")

class RowButtons(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Hi", style=ButtonStyle.red)
    async def first_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("이것은 1번째 버튼입니다.")

    @disnake.ui.button(label="this is", style=ButtonStyle.red)
    async def second_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("이것은 2번째 버튼입니다.")

    @disnake.ui.button(label="a row of", style=ButtonStyle.blurple, row=1)
    async def third_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("이것은 3번째 버튼입니다.")

    @disnake.ui.button(label="buttons.", style=ButtonStyle.blurple, row=1)
    async def fourth_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("이것은 4번째 버튼입니다.")

    @disnake.ui.button(emoji="🥳", style=ButtonStyle.green, row=2)
    async def fifth_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("이것은 5번째 버튼입니다.")


@bot.command()
async def buttons(ctx):
    await ctx.send("여기 몇개의 버튼이 있어요!", view=RowButtons())

bot.run("token")