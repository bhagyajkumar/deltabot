import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class DeltaBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


bot = DeltaBot(command_prefix="d,")

@bot.event
async def on_ready():
    print("bot is online")

cogs = [
    "cogs.test"
]

if __name__ == "__main__":
    bot.run(os.environ.get("BOT_TOKEN"))