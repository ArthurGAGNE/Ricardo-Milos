import discord
from discord.ext import commands

print("Demarrage en cours...")

#bot config
bot = commands.Bot(command_prefix="!")
token = "ODc5NzczNjQwMzc4NDQ5OTQw.YSUnDQ.v57cMQ5Mcjy5abJh5LpXvAsHCVI"
delete_message_delay=5


@bot.event
async def on_ready():
    print("Le bot est prêt.")

@bot.event
async def on_member_join(member):
    print(f"L'utilisateur {member.display_name} a rejoint le serveur !")

@bot.command(name="ping")
async def ping(ctx):
	await ctx.message.delete()
	await ctx.send("pong", delete_after=delete_message_delay)

@bot.command(name="avatar")
async def avatar(ctx, avamember : discord.Member=None):
	await ctx.message.delete();
	embed = discord.Embed(title = f"**Avatar**", description = f"*Demande de l'avatar*",color = 0xfd7e08)
	embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
	embed.set_image(url=avamember.avatar_url)
	embed.add_field(name = "Cible", value = avamember.name, inline = False)
	embed.add_field(name = "URL", value = avamember.avatar_url, inline = False)
	await ctx.send(embed = embed)

bot.run(token)