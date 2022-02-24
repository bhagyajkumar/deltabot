from discord.ext import commands
from main import DeltaBot

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Hello")


def setup(bot:DeltaBot):
    bot.add_cog(TestCog(bot))