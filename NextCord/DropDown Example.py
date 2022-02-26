import nextcord

from nextcord.ext import commands

class Dropdown(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(label='빨강', description='당신이 고른 색깔은 빨강입니다.', emoji='🟥'),
            nextcord.SelectOption(label='초록', description='당신이 고른 색깔은 초록입니다.', emoji='🟩'),
            nextcord.SelectOption(label='파랑', description='당신이 고른 색깔은 파랑입니다.', emoji='🟦')
        ]
        super().__init__(placeholder='가장 좋아하는 색깔을 골라주세요.', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f'당신이 고른 색깔은 {self.values[0]}입니다.')


class DropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())


bot = commands.Bot(command_prefix='!')


@bot.command()
async def colour(ctx):
    view = DropdownView()
    await ctx.send('당신이 고른색깔 :', view=view)


bot.run('token')