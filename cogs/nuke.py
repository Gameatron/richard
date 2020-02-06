import discord
from discord.ext import commands
import json


class Nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open("info.json", 'r') as f:
            self.leaders = json.load(f)["leaders"]

    def check(self, ctx):
        if ctx.author.id in self.leaders:
            return True
        return False

    @commands.command()
    async def epilepsy(self, ctx, user: discord.Member):
        await ctx.message.delete()
        m = await ctx.send(f"Epilepsy attack started on {user.mention}.")
        e = discord.Embed()
        e.set_image(url="https://media.giphy.com/media/J6eabmqUY5NFS/giphy.gif")
        if self.check:
            for _ in range(10):
                await user.send(embed=e)
        await m.edit(content=f"Done with the epilepsy attack, {ctx.author.mention}.")


def setup(bot):
    bot.add_cog(Nuke(bot))
