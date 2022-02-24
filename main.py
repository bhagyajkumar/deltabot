import asyncio
import os
from discord.ext import commands
from dotenv import load_dotenv
import asyncpg

load_dotenv()

class DeltaBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.db = self.get_db()
        super().__init__(*args, **kwargs)

    def get_db(self):
        db_credentials = {
            "host": os.environ.get("POSTGRES_HOST"),
            "user": os.environ.get("POSTGRES_USER"),
            "password": os.environ.get("POSTGRES_PASSWORD"),
            "database": os.environ.get("POSTGRES_DATABASE"),
        }
        return asyncio.get_event_loop().run_until_complete(asyncpg.create_pool(min_size=1,max_size=3,**db_credentials))


bot = DeltaBot(command_prefix="d,")

@bot.event
async def on_ready():
    print("bot is online")

cogs = [
    "cogs.test",
    "cogs.owner",
    "jishaku"
]

for cog in cogs:
    bot.load_extension(cog)

if __name__ == "__main__":
    bot.run(os.environ.get("BOT_TOKEN"))