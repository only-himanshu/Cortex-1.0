from discord.ext import commands
from utils.brain import generate_roast

class roast(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roast(self,ctx):
        try:
            roast = generate_roast()
            await ctx.send(roast)
        except Exception as e:
            await ctx.send("Not enough data to roast yet")        

async def setup(bot):
    await bot.add_cog(roast(bot))
                