import discord
from discord.ext import commands
import os
import keep_alive
import json
from commands import dangan
from commands import male
from commands import female

def get_prefix(client,message):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix=get_prefix)

@client.event
async def on_guild_join(guild):


    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "-"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)




@client.command()
@commands.has_permissions(administrator = True)
async def changeprefix(ctx, prefix):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)    

    await ctx.send(f"The prefix was changed to {prefix}")

client.remove_command("help")

@client.group(invoke_without_command=True)
async def help(ctx):
        em = discord.Embed(title = "Kokichi Help", description = "a KxngBots creation", colour = discord.Colour.dark_purple())

        em.add_field(name="dev", value="Returns developer's Twitter account.")
        em.add_field(name="support", value="Returns an invite to the support server.")
        em.add_field(name="ping", value="Check Kokichi's latency")
        em.add_field(name="changeprefix", value="Change Kokichi's server prefix (requires Administrator permissions)")
        em.add_field(name = "boy", value = "Rolls a random Danganronpa boy from any of the 4 games.")
        em.add_field(name = "girl", value = "Rolls a random girl from any of the 4 games.")        
        em.add_field(name = "roll", value = "Rolls a random character from any of the 4 games.")
        em.add_field(name="kaito, maki, shuichi, dice, pressure", value="Kokichi will react to these keywords")


        await ctx.send(embed = em)

#Bot Loading

@client.event
async def on_ready():
    print("Remeber Xander. He's his own bot. He's not Nagito 2. He's Kokichi. Only you know what you've built. Only you know. So go out and give em hell! Just like we planned!")
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game('-help | Version 1.2.1'))



#Commands

@client.command()
async def ping(ctx):
        await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

@client.command()
async def roll(ctx):
        await ctx.send(dangan())

@client.command()
async def boy(ctx):
        await ctx.send(male())

@client.command()
async def girl(ctx):
        await ctx.send(female())

@client.command()
async def support(ctx):
        await ctx.send("Support server: https://discord.gg/HR2Jej5NaB ")

@client.command()
async def dev(ctx):
        await ctx.send("Check out my developer on Twitter! https://twitter.com/KxngBots")

@client.event
async def on_message(msg):
        if "pressure" in msg.content:
                await msg.add_reaction('😖')

        if "dice" in msg.content:
                await msg.add_reaction('🎲')
        
        if "shuichi" in msg.content:
                await msg.add_reaction('🏃🏾‍♂️')
        
        if " maki" in msg.content:
                await msg.add_reaction('🙈')
        
        if "kaito" in msg.content:
                await msg.add_reaction('🙄')

        await client.process_commands(msg)


#Keep Alive

keep_alive.keep_alive()

#Token

TOKEN = os.environ.get("TOKEN")

client.run(TOKEN)
