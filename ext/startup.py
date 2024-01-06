from discord.ext import commands
import asyncpg
import os


class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        self.bot.db = await asyncpg.connect(
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASS"],
            database=os.environ["DB_NAME"],
            host=os.environ["DB_HOST"]
        )


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user.name} | {self.bot.user.id}')


async def setup(bot):
    await bot.add_cog(Startup(bot))