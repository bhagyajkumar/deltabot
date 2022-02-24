from discord.ext import commands
from main import DeltaBot
import time
import discord
class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        websocket_latency = self.bot.latency * 1000
        dbt1 = time.time()
        await self.bot.db.fetchval("SELECT 1")
        database_latency = (time.time() - dbt1) * 1000
        embed = discord.Embed(title="PIng", color=self.bot.default_color)
        embed.add_field(name="websocket Latency", value=f"```js\n{str(round(websocket_latency))} ms```", inline=False)
        embed.add_field(name="database latency", value=f"```js\n{str(round(database_latency))} ms```", inline=False)
        mest1 = time.time()
        mes = await ctx.send(embed=embed)
        message_latency = (time.time() - mest1) * 1000
        embed.add_field(name="Typing", value=f"```js\n{str(round(message_latency))} ms```")
        await mes.edit(embed=embed)



def setup(bot:DeltaBot):
    bot.add_cog(TestCog(bot))