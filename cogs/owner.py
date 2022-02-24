import asyncio
import discord
from discord.ext import commands
from prettytable import PrettyTable


class Owner(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def pull(self, ctx):
        proc = await asyncio.create_subprocess_shell("git pull origin main", stdout=asyncio.subprocess.PIPE,
                                                     stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await proc.communicate()
        stdout = f"{stdout.decode()}" if stdout != b"" else ""
        stderr = f"\n{stderr.decode()}" if stderr != b"" else ""
        final = f"```\n{stdout}\n{stderr}\n```"
        embed = discord.Embed(color=discord.Color.blurple(), title="Pulling from GitHub...",
                              description=final)
        return await ctx.send(embed=embed)

    @commands.is_owner()
    @commands.command()
    async def sql(self, ctx, *, command):
        res = await self.bot.db.fetch(command)
        if len(res) == 0:
            return await ctx.send("Query finished successfully No results to display")
        headers = list(res[0].keys())
        table = PrettyTable()
        table.field_names = headers
        for record in res:
            lst = list(record)
            table.add_row(lst)
        msg = table.get_string()
        paginator = commands.Paginator()
        for line in msg.split("\n"):
            paginator.add_line(line)
        for page in paginator.pages:
            await ctx.send(page)


def setup(bot):
    bot.add_cog(Owner(bot))
