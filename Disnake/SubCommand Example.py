import disnake
from disnake.ext import commands

bot = commands.Bot("!")

@bot.slash_command()
async def command(inter):
    print("이 코드는 하위 명령이 호출될 때마다 실행됩니다.")


@command.sub_command()
async def foo(inter, option: str):
    await inter.response.send_message(f"{option}을 받았어요")


@command.sub_command()
async def bar(inter, option: int):
    await inter.response.send_message(f"{option}을 받았어요")


class MyCog(commands.Cog):
    @commands.slash_command()
    async def command(self, inter):
        print("이 코드는 하위 명령이 호출될 때마다 실행됩니다.")

    @command.sub_command_group()
    async def foo(self, inter):
        print("이 코드는 하위 명령이 호출될 때마다 실행됩니다.")

    @foo.sub_command()
    async def a(self, inter, option: int):
        await inter.response.send_message(f"/command foo를 실행했습니다. {option}")

    @command.sub_command_group()
    async def bar(self, inter):
        print("이 코드는 Bar의 하위 명령이 호출될 때마다 실행됩니다.")

    @bar.sub_command()
    async def b(self, inter, option: float):
        await inter.response.send_message(f"/command bar b를 실행했습니다. {option}")