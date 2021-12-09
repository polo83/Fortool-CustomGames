import discord
from discord.ext import commands
import asyncio

class Roles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='setup',
        description='Commande pour créer des salons. Pour effectuer cette commande il vous faudras les permissions administrateur !'
    )

    @commands.Cog.listener()
    @commands.has_permissions(administrator = True)
    async def roles(self, ctx):
        await ctx.guild.create_role(name="✅ valid")
        await ctx.channel.send('Configuration terminée ! Vous pouvez exécutez la commande "*register" pour pouvoir vous inscrire !')
        guild = ctx.message.guild
        setup = await ctx.guild.create_category("CUSTOM GAMES SYSTEME")
        await guild.create_text_channel("📢┆annonces",category=setup)
        await guild.create_text_channel("📩┆request",category=setup)
def setup(bot):
    bot.add_cog(Roles(bot))