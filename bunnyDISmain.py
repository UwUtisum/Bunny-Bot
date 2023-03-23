#/* Copyright (C) 2021 Leah Kemp - All Rights Reserved
import tweepy
import time
import random
import discord
import requests
import json
import math
import os
import asyncio
import asyncpraw
from discord_slash import SlashCommand
from discord_slash.utils import manage_commands
from discord_slash import SlashContext
from discord.ext import commands
from secrets import randbelow
from pathlib import Path
from discord.ext.commands import CommandNotFound
from colorama import Fore, Back, Style
from colorama import init
init()
#---------------------------------------------------------------twitter auth--------------------------------------------------------------
auth = tweepy.OAuthHandler("", "")#REMOVED 
auth.set_access_token("", "")#REMOVED 
api = tweepy.API(auth)
prefix = ">"
bot = commands.Bot(command_prefix = prefix)
embedhelp = discord.Embed()
embed = discord.Embed(color=0xFDADFD)
em = discord.Embed(color=0xFDADFD) #creates embed
bot.remove_command("help") #REMEMBER CLIENT = BOT!!!!!!!!!!

#exstentions = ["cogs.memes"]# "cogs.misc", "cogs.money", "cogs.roleplay", "cogs.songs"]
#if __name__ == "__main__":
 #  for exstention in exstentions:
#        bot.load_extension(exstention)
blacklist = [815929634235088947, 99153250015518720, 601057288958115848 ,701696539021541436, 139412744439988224, 136583532972605440, 384083999435259905, 300695488414351362, 424510595702718475, 248324194436251658, 150417106549211136, 300438546236571658, 212530298259374080, 715520615896842302, 189759562910400512, 311553339261321216, 221221226561929217, 254814547326533632, 141075183271280641, 253233185800847361, 608767196839018507, 125492204234997761, 205680187394752512, 286166184402092042, 599174147796631572, 479729829164351499, 592742184919236628, 585923878023462923, 324589359439413248, 738758679423090698, 640995402958766090, 370726688314753056, 686008194253848583]
#--------------------------------------------------------------------slash command----------------------------------------------------------
slash = SlashCommand(bot)# auto_register=True
@slash.slash(name="bunnyhelp")
async def bunnyhelp(ctx: SlashContext):
    embedhelp = discord.Embed(description=f"""list of commands ^-^:
**-new econamy commands please use the command below to see how to use them ^-^-**
**>bunnybuckscommands** ☁。lists commands for bunnys econamy
**---------------------------------------------**
**>meme** ☁。this command sends you a random wholesome meme. ^-^ 
**>recommendsong** ☁。this command gives you a kawaii music recomendation
**>stickbug** ☁。sends the user a get stick bugged meme :3
**>damedane** ☁。sends a deep fake video of isabelle from animal crossing singing dame dane (thank you to biscuit.bot on instagram for the meme ^-^)
**>hornyjail** ☁。bonks the user on the head for being the horny >:(
**>poggers** ☁。poggers in chat
**>invitelink** ☁。gives the user a invite link to add bunny to other servers ^-^
**>conga** ☁。brain go brrrrr
**>recomendgame** ☁。recomends the user a random steam game :3
**>love** ☁。sends love to another user via there @ exsample: >love @bunny#7957
**>hug** ☁。hugs another user via there @ exsample: >hug @bunny#7957
**>kiss** ☁。slaps another user via there @ exsample: >kiss @bunny#7957
**>cry** ☁。this shows the user is crying 
**>homiekiss** ☁。kiss yo homie good night via there @ exsample: >homiekiss @bunny#7957
~~**>toasterbath** ☁。makes the user commit toaster bath :P.~~ **(disabled)**
**>warcrimes** ☁。makes the user commit war crimes >:3.
**>coffee** ☁。make another user a cup of coffee via there @ exsample: >coffee @bunny#7957
**>slap** ☁。slaps another user via there @ exsample: >slap @bunny#7957
**>kill** ☁。kills another user via there @ exsample: >kill @bunny#7957
**>bunnyteam** ☁。displays a message with the crdits of bunny bot ^-^
**-------------------------------------------------------------------------------**
if you guys want to help me out pay the server costs to keep bunny runing please use my paypal linked below **you dont have to donate and bunny is fully free to use! (i hate bots with premium)**
https://www.paypal.me/uwutisum""",color=0xFDADFD)
    await ctx.channel. send(content=f"bunnyhelp", embed=embedhelp)
    embedhelp = discord.Embed(description=f"""**Update:**New tamagotchi minigame progress update!**
*everything is coded into bunny im just waiting on some artwork to come in and as soon as i have that i will update you guys when it is ready for releace*""",color=0xFDADFD)
    await ctx.channel.send(content=f"bunnyhelp",embed=embedhelp)

#------------------------------------------------------------------------money--------------------------------------------------------------
if os.path.exists('candy.json'):
    with open('candy.json', 'r') as file:
        candy = json.load(file)
else:
    candy = {}
if os.path.exists('amounts.json'):
    with open('amounts.json', 'r') as file:
        amounts = json.load(file)
else:
    pets = {}
if os.path.exists('pets.json'):
    with open('pets.json', 'r') as file:
        pets = json.load(file)
else:
    pets = {}
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

#@bot.event
#async def on_command_error(ctx, error):
    #if isinstance(error, MissingRequiredArgument):
     #   return
    #raise error

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("spreading love everyday in " + str(len(bot.guilds)) + " servers, please use '>help' to see a list of commands ^-^"))#https://youtu.be/04854XqcfCY spreading love everyday in " + str(len(bot.guilds)) + " servers, please use '>help' to see a list of commands ^-^
    print("bunny has connected to discord! ^-^")
    global candy
    try:
        with open('candy.json') as f:
            candy = json.load(f)
    except FileNotFoundError:
        print("Could not load candy.json")
        candy = {}  
    global amounts
    try:
        with open('amounts.json') as f:
            amounts = json.load(f)
    except FileNotFoundError:
        print("Could not load amounts.json")
        amounts = {}
    global pets
    try:
        with open('pets.json') as f:
            pets = json.load(f)
    except FileNotFoundError:
        print("Could not load pets.json")
        pets = {}

def _savepets():
    with open('pets.json', 'w+') as f:
        json.dump(pets, f)

def _savecandy():
    with open('candy.json', 'w+') as f:
        json.dump(candy, f)

def _save():
    with open('amounts.json', 'w+') as f:
        json.dump(amounts, f)
#-------------------------------------------------------next launch command -------------------------------------------------------
@bot.command(pass_context=True)
async def nextlaunch(ctx):
    if ctx.author.id in blacklist:
        primary_id = str(ctx.message.author.id)
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used nextlaunch command")
        if id in amounts:
            amounts[id] += 100
            response = requests.get("https://fdo.rocketlaunch.live/json/launches/next/1")
            r_dict = response.json()
            embed=discord.Embed(title= r_dict["result"][0]["vehicle"]["name"], description= r_dict["result"][0]["launch_description"], color=0x7e29ff)
            embed.set_image(url="https://www.spaceflightinsider.com/wp-content/uploads/hangar/header/falcon-9.jpg")
            embed.set_author(name= r_dict["result"][0]["slug"])
            embed.set_footer(text="Data from www.rocketlaunch.live")
            await ctx.send(embed=embed)
        else:
            embedmoney1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please do **>register** to make a account",color=0xFDADFD)
            embedmoney1.set_image(url="https://38.media.tumblr.com/87ee87bd32c8050aead01b1826676581/tumblr_mt6e1d1k7A1ssrmb2o1_500.gif")
            await ctx.send(embed=embedmoney1)
#-------------------------------------------------------balance command-------------------------------------------------------
@bot.command(pass_context=True)
async def balance(ctx):
    if ctx.author.id in blacklist:
        primary_id = str(ctx.message.author.id)
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used balance command")
        if id in amounts:
            embedmoney = discord.Embed(description="You have {} in the bank".format(amounts[id]),color=0xFDADFD)
            embedmoney.set_image(url="https://media.tenor.co/images/ec2c2851f47f55eaa04293187c202ebb/raw")
            await ctx.send(embed=embedmoney)
        else:
            embedmoney1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please do **>register** to make a account",color=0xFDADFD)
            embedmoney1.set_image(url="https://38.media.tumblr.com/87ee87bd32c8050aead01b1826676581/tumblr_mt6e1d1k7A1ssrmb2o1_500.gif")
            await ctx.send(embed=embedmoney1)
#---------------------------------------------------------------------------------------------
@bot.command(pass_context=True)
async def register(ctx):
    if ctx.author.id in blacklist:
        primary_id = str(ctx.message.author.id)
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        if id not in amounts:
            amounts[id] = 100000
            embedreg1 = discord.Embed(description=f"{ctx.author.mention}<:candy8634:772148204723765259>You are now registered you have been granted **100k** as a welcome gift ^-^<:candy8634:772148204723765259>",color=0xFDADFD)
            embedreg1.set_image(url="https://i.gifer.com/7u4S.gif")
            await ctx.send(embed=embedreg1)
            print("["+ Fore.YELLOW + 'New User' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL +" signed up with bunny!")
            _save()
        else:
            embedreg2 = discord.Embed(description=f"{ctx.author.mention} You already have an account :P.",color=0xFDADFD)
            embedreg2.set_image(url="http://gifimage.net/wp-content/uploads/2017/09/anime-facepalm-gif-4.gif")
            await ctx.send(embed=embedreg2)
#----------------------------------------------------------------transfer command----------------------------------------------------------------
@bot.command(pass_context=True)
async def transfer(ctx, amount: int, other: discord.Member):
    primary_id = str(ctx.message.author.id)
    other_id = str(other.id)
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " transfered " + Fore.YELLOW + str(amount) + Style.RESET_ALL + " to "+ Fore.YELLOW + other_id + Style.RESET_ALL)
        if amount > 0:
            if primary_id not in amounts:
                embedtran1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
                embedtran1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
                await ctx.send(embed=embedtran1)
            elif other_id not in amounts:
                embedtran2 = discord.Embed(description=f"{other.mention} does not have an account",color=0xFDADFD)
                embedtran2.set_image(url="https://media.giphy.com/media/GPQzOZyCFJq0M/giphy.gif")
                await ctx.send(embed=embedtran2)
            elif amounts[primary_id] < amount:
                embedtran3 = discord.Embed(description=f"{ctx.author.mention} You cannot afford this transaction",color=0xFDADFD)
                embedtran3.set_image(url="https://media1.tenor.com/images/f7e52d33e39f4d91cd6c00da062e17fc/tenor.gif?itemid=4874884")
                await ctx.send(embed=embedtran3)
            else:
                amounts[primary_id] -= amount
                amounts[other_id] += amount
                embedtran4 = discord.Embed(description=f"{ctx.author.mention} transaction complete",color=0xFDADFD)
                embedtran4.set_image(url="https://media1.tenor.com/images/3f685bc7226929d5d41ff88643b4f557/tenor.gif?itemid=7547149")
                await ctx.send(embed=embedtran4)
            _save()
        elif amount < 0:
            await ctx.send("**invalid number**")
#----------------------------------------------------------------cointoss command----------------------------------------------------------------   
@bot.command(pass_context=True)
async def cointoss(ctx, amount: int):
    primary_id = str(ctx.message.author.id)
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used cointoss command")
        if amount > 0:
            if primary_id not in amounts: 
                embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
                embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
                await ctx.send(embed=embedcoin1)
            elif amounts[primary_id] < amount:
                embedtran3 = discord.Embed(description=f"{ctx.author.mention} You cannot afford this transaction",color=0xFDADFD)
                embedtran3.set_image(url="https://media1.tenor.com/images/f7e52d33e39f4d91cd6c00da062e17fc/tenor.gif?itemid=4874884")
                await ctx.send(embed=embedtran3)
            else:
                t = (randbelow(2))
                if t == 0:
                    amounts[primary_id] += amount 
                    embedtran4 = discord.Embed(description=f"{ctx.author.mention} Yayyyyy ^-^ you win **{amount}**",color=0xFDADFD)
                    embedtran4.set_image(url="https://media1.tenor.com/images/3f685bc7226929d5d41ff88643b4f557/tenor.gif?itemid=7547149")
                    await ctx.send(embed=embedtran4)
                elif t == 1:
                    amounts[primary_id] -= amount 
                    embedtran4 = discord.Embed(description=f"{ctx.author.mention} OnO u lost **{amount}**",color=0xFDADFD)
                    embedtran4.set_image(url="https://media1.tenor.com/images/3f685bc7226929d5d41ff88643b4f557/tenor.gif?itemid=7547149")
                    await ctx.send(embed=embedtran4)
                elif amounts[primary_id] == amount:
                    embedtran4 = discord.Embed(description=f"{ctx.author.mention} you can not gamble all your money",color=0xFDADFD)
                    embedtran4.set_image(url="https://media1.tenor.com/images/3f685bc7226929d5d41ff88643b4f557/tenor.gif?itemid=7547149")
            _save()
        elif amount < 0:
            await ctx.send("**invalid number**")
#------------------------------------------------------------pet number codeing-------------------------------------------------------------------
#0 = dead or no pet
#1 = cat normal
#2 = cat hungry
#3 = cat thirsty
#4 = cat hungry + thirsty
#5 = bunny normal
#6 = bunny hungry
#7 = bunny thirsty
#8 = bunny hungry + thirsty
#9 = hamster normal
#10 = hamster hungry
#11 = hamster thirsty
#12 = hamster hungry + thirsty
#13 = bird normal
#14 = bird hungry
#15 = bird thirsty
#16 = bird hungry + thirsty
#----------------------------------------------------------------pet shop-------------------------------------------------------------------------
@bot.command(pass_context = True)
async def buypet(ctx):
    if ctx.author.id in blacklist:
        primary_id = str(ctx.message.author.id)
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used buypet command")
        if id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            x = 2
            if x == 1:
                print("fuck")
            else:
                amounts[id] += 100
                embedcoin1 = discord.Embed(description=f"{ctx.author.mention} are you sure you want to buy a pet :D for **100k** or **5 peaces candy** please enter **yes or no**",color=0xFDADFD)
                embedcoin1.set_image(url="https://66.media.tumblr.com/e33e4d237e767978ceaaced1f2bdf393/tumblr_o4wssfL0451u8eo0po1_500.gif")
                await ctx.send(embed=embedcoin1)
                msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
                if msg.content.lower() == "yes":
                    id = str(ctx.message.author.id)
                    embedcoin1 = discord.Embed(description=f"{ctx.author.mention} how do you want to pay ^-^ please enter **cash or candy**",color=0xFDADFD)
                    embedcoin1.set_image(url="https://66.media.tumblr.com/e33e4d237e767978ceaaced1f2bdf393/tumblr_o4wssfL0451u8eo0po1_500.gif")
                    await ctx.send(embed=embedcoin1)
                    msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
#----------------------------------------------------------------pay in candy-------------------------------------------------------------------------
                    if msg.content.lower() == "candy":
                        if id not in candy:
                            await ctx.send("**you do not have any peaces of candy**")
                        else:
                            embedcoin1 = discord.Embed(description=f"""{ctx.author.mention} what pet do you want ^-^
**Cat** 
**bunny** 
**kowala** 
**bird**""",color=0xFDADFD)
                            await ctx.send(embed=embedcoin1)
                            msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
                            if msg.content.lower() == "cat":
                                embedcoin1 = discord.Embed(description=f"{ctx.author.mention} are you sure you want to buy a **cat** for **5 peaces of candy** ^-^ (image place holder)",color=0xFDADFD)
                                embedcoin1.set_image(url="https://media1.giphy.com/media/DoIquD1MhDGMw/giphy.gif")
                                await ctx.send(embed=embedcoin1)
                                msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
                                if msg.content.lower() == "yes":
                                    if id not in candy: 
                                        await ctx.send("OnO u dont have any candy")
                                    if id in candy:
                                        if candy[id] > 5:
                                            if id in pets:
                                                if pets[id] > 0:
                                                    await ctx.send("**you already have a pet**")
                                                else:
                                                    candy[id] -= 5
                                                    pets[id] = 4
                                                    _savepets()
                                                    _savecandy()
                                                    await ctx.send("congrats you now have a pet **cat**")
                                            elif id not in pets:
                                                candy[id] -= 5
                                                pets[id] = 4
                                                _savepets()
                                                _savecandy()
                                                await ctx.send("congrats you now have a pet **cat**")
                                        elif candy[id] < 5:
                                            await ctx.send("OnO you dont have enough candy")
                                elif msg.content.lower() == "no":
                                    await ctx.send("transaction canceled")

                            elif msg.content.lower() == "bunny":
                                embedcoin1 = discord.Embed(description=f"{ctx.author.mention} are you sure you want to buy a **bunny** for **5 peaces of candy** ^-^ (image place holder)",color=0xFDADFD)
                                embedcoin1.set_image(url="https://data.whicdn.com/images/290253428/original.gif")
                                await ctx.send(embed=embedcoin1)
                                msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
                                if msg.content.lower() == "yes":
                                    if id not in candy: 
                                        await ctx.send("OnO u dont have any candy")
                                    if id in candy:
                                        if candy[id] > 5:
                                            if id in pets:
                                                if pets[id] > 0:
                                                    await ctx.send("**you already have a pet**")
                                                else:
                                                    candy[id] -= 5
                                                    pets[id] = 8
                                                    _savepets()
                                                    _savecandy()
                                                    await ctx.send("congrats you now have a pet **bunny**")
                                            elif id not in pets:
                                                candy[id] -= 5
                                                pets[id] = 8
                                                _savepets()
                                                _savecandy()
                                                await ctx.send("congrats you now have a pet **bunny**")
                                        elif candy[id] < 5:
                                            await ctx.send("OnO you dont have enough candy")
                                elif msg.content.lower() == "no":
                                    await ctx.send("transaction canceled")

                            elif msg.content.lower() == "kowala":
                                embedcoin1 = discord.Embed(description=f"{ctx.author.mention} are you sure you want to buy a **kowala** for **5 peaces of candy** ^-^ (image place holder)",color=0xFDADFD)
                                embedcoin1.set_image(url="https://data.whicdn.com/images/235038651/original.gif")
                                await ctx.send(embed=embedcoin1)
                                msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
                                if msg.content.lower() == "yes":
                                    if id not in candy: 
                                        await ctx.send("OnO u dont have any candy")
                                    if id in candy:
                                        if candy[id] > 5:
                                            if id in pets:
                                                if pets[id] > 0:
                                                    await ctx.send("**you already have a pet**")
                                                else:
                                                    candy[id] -= 5
                                                    pets[id] = 12
                                                    _savepets()
                                                    _savecandy()
                                                    await ctx.send("congrats you now have a pet **kowala**")
                                            elif id not in pets:
                                                candy[id] -= 5
                                                pets[id] = 12
                                                _savepets()
                                                _savecandy()
                                                await ctx.send("congrats you now have a pet **kowala**")
                                        elif candy[id] < 5:
                                            await ctx.send("OnO you dont have enough candy")
                                elif msg.content.lower() == "no":
                                    await ctx.send("transaction canceled")

                            elif msg.content.lower() == "bird":
                                embedcoin1 = discord.Embed(description=f"{ctx.author.mention} are you sure you want to buy a **bird** for **5 peaces of candy** ^-^ (image place holder)",color=0xFDADFD)
                                embedcoin1.set_image(url="https://data.whicdn.com/images/290016715/original.gif")
                                await ctx.send(embed=embedcoin1)
                                msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
                                if id not in candy: 
                                    await ctx.send("OnO u dont have any candy")
                                if id in candy:
                                    if candy[id] > 5:
                                        if id in pets:
                                            if pets[id] > 0:
                                                await ctx.send("**you already have a pet**")
                                            else:
                                                candy[id] -= 5
                                                pets[id] = 16
                                                _savepets()
                                                _savecandy()
                                                await ctx.send("congrats you now have a pet **bird**")
                                        elif id not in pets:
                                            candy[id] -= 5
                                            pets[id] = 16
                                            _savepets()
                                            _savecandy()
                                            await ctx.send("congrats you now have a pet **bird**")
                                        elif candy[id] < 5:
                                            await ctx.send("OnO you dont have enough candy")
                                elif msg.content.lower() == "no":
                                    await ctx.send("transaction canceled")
#----------------------------------------------------------------pay in cash-------------------------------------------------------------------------
                    if msg.content.lower() == "cash":
                        embedcoin1 = discord.Embed(description=f"""{ctx.author.mention} what pet do you want ^-^
**Cat** 
**bunny** 
**kowala** 
**bird**""",color=0xFDADFD)
                        await ctx.send(embed=embedcoin1)
                        msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
                        if msg.content.lower() == "cat":
                            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} are you sure you want to buy a **cat** for **100000 bunny bucks** ^-^ (image place holder)",color=0xFDADFD)
                            embedcoin1.set_image(url="https://media1.giphy.com/media/DoIquD1MhDGMw/giphy.gif")
                            await ctx.send(embed=embedcoin1)
                            msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
                            if msg.content.lower() == "yes":
                                if id in amounts:
                                    if amounts[id] > 100000:
                                        if id in pets:
                                            if pets[id] > 0:
                                                await ctx.send("**you already have a pet**")
                                            else:
                                                candy[id] -= 100000
                                                pets[id] = 4
                                                _savepets()
                                                _savecandy()
                                                await ctx.send("congrats you now have a pet **cat**")
                                        elif id not in pets:
                                            candy[id] -= 100000
                                            pets[id] = 4
                                            _savepets()
                                            _savecandy()
                                            await ctx.send("congrats you now have a pet **cat**")
                                    elif candy[id] < 100000:
                                        await ctx.send("OnO you dont have enough bunny bucks")
                            elif msg.content.lower() == "no":
                                await ctx.send("transaction canceled")

                        elif msg.content.lower() == "bunny":
                            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} are you sure you want to buy a **bunny** for **100000 bunny bucks** ^-^ (image place holder)",color=0xFDADFD)
                            embedcoin1.set_image(url="https://data.whicdn.com/images/290253428/original.gif")
                            await ctx.send(embed=embedcoin1)
                            msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
                            if msg.content.lower() == "yes":
                                if id in amounts:
                                    if amounts[id] > 100000:
                                        if id in pets:
                                            if pets[id] > 0:
                                                await ctx.send("**you already have a pet**")
                                            else:
                                                candy[id] -= 100000
                                                pets[id] = 8
                                                _savepets()
                                                _savecandy()
                                                await ctx.send("congrats you now have a pet **bunny**")
                                        elif id not in pets:
                                            candy[id] -= 100000
                                            pets[id] = 8
                                            _savepets()
                                            _savecandy()
                                            await ctx.send("congrats you now have a pet **bunny**")
                                    elif candy[id] < 100000:
                                        await ctx.send("OnO you dont have enough bunny bucks")
                            elif msg.content.lower() == "no":
                                await ctx.send("transaction canceled")

                        elif msg.content.lower() == "kowala":
                            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} are you sure you want to buy a **kowala** for **100000 bunny bucks** ^-^ (image place holder)",color=0xFDADFD)
                            embedcoin1.set_image(url="https://data.whicdn.com/images/235038651/original.gif")
                            await ctx.send(embed=embedcoin1)
                            msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
                            if msg.content.lower() == "yes":
                                if id in amounts:
                                    if amounts[id] > 100000:
                                        if id in pets:
                                            if pets[id] > 0:
                                                await ctx.send("**you already have a pet**")
                                            else:
                                                candy[id] -= 100000
                                                pets[id] = 12
                                                _savepets()
                                                _savecandy()
                                                await ctx.send("congrats you now have a pet **kowala**")
                                        elif id not in pets:
                                            candy[id] -= 100000
                                            pets[id] = 12
                                            _savepets()
                                            _savecandy()
                                            await ctx.send("congrats you now have a pet **kowala**")
                                    elif candy[id] < 100000:
                                        await ctx.send("OnO you dont have enough bunny bucks")
                            elif msg.content.lower() == "no":
                                await ctx.send("transaction canceled")

                        elif msg.content.lower() == "bird":
                            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} are you sure you want to buy a **bird** for **100000 bunny bucks** ^-^ ",color=0xFDADFD)
                            embedcoin1.set_image(url="https://i.imgur.com/pgsglFb.png")
                            await ctx.send(embed=embedcoin1)
                            msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
                            if msg.content.lower() == "yes":
                                if id in amounts:
                                    if amounts[id] > 100000:
                                        if id in pets:
                                            if pets[id] > 0:
                                                await ctx.send("**you already have a pet**")
                                            else:
                                                amounts[id] -= 100000
                                                pets[id] = 16
                                                _savepets()
                                                _save()
                                                embedcoin1 = discord.Embed(description=f"{ctx.author.mention} congrats you now have a pet **bird** please use the commands **>feedpet** and **>waterpet** to give food and water to your pet, you can also **>train** your pet which makes it level up ^-^ **the higher the level the more bunny bucks you earn**",color=0xFDADFD)
                                                embedcoin1.set_image(url="https://i.imgur.com/VebZjo6.png")
                                                await ctx.send(embed=embedcoin1)
                                        elif id not in pets:
                                            amounts[id] -= 100000
                                            pets[id] = 16
                                            _savepets()
                                            _save()
                                            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} congrats you now have a pet **bird** please use the commands **>feedpet** and **>waterpet** to give food and water to your pet, you can also **>train** your pet which makes it level up ^-^ **the higher the level the more bunny bucks you earn**",color=0xFDADFD)
                                            embedcoin1.set_image(url="https://i.imgur.com/VebZjo6.png")
                                            await ctx.send(embed=embedcoin1)
                                    elif amounts[id] < 100000:
                                        await ctx.send("OnO you dont have enough bunny bucks")
                            elif msg.content.lower() == "no":
                                await ctx.send("transaction canceled")
                elif msg.content.lower() == "no":
                    await ctx.send("transaction canceled")
#------------------------------------------------------------pet viewer----------------------------------------------------------------- 
@bot.command(pass_context = True)
async def pet(ctx):
    if ctx.author.id in blacklist:
        primary_id = str(ctx.message.author.id)
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the pet command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            if primary_id not in pets:
                await ctx.send("OnO you do not have a pet")
            else:
                if pets[primary_id] == 0:
                    soldpet = randbelow(2)
                    if soldpet == 0:
                        embedcoin1 = discord.Embed(description=f"OnO {ctx.author.mention} it looks like your pet eather ran away or you sold it",color=0xFDADFD)
                        embedcoin1.set_image(url="https://i.imgur.com/sdagrP9.png")
                        await ctx.send(embed=embedcoin1)
                    elif soldpet == 1:
                        embedcoin1 = discord.Embed(description=f"OnO {ctx.author.mention} it looks like your pet eather ran away or you sold it",color=0xFDADFD)
                        embedcoin1.set_image(url="https://i.imgur.com/nMGMyd9.png")
                        await ctx.send(embed=embedcoin1)
                elif pets[primary_id] == 1:
                    await ctx.send("ONO I MADE A FUCKY WUCKY")

#---------------------------------------------------------------sell pet---------------------------------------------------------------

@bot.command(pass_context = True)
async def sellpet(ctx):
    if ctx.author.id in blacklist:
        primary_id = str(ctx.message.author.id)
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used sell pet command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            if id not in pets:
                await ctx.send("you do not have a pet right now please use **>buypet** to buy a pet ^-^")
            else:
                if pets[id] == 0:
                    await ctx.send("OnO ")
                else:
                    return

#with open('daily', 'r') as f:
  #  daily = eval(f.read())

#def save_daily():
 #   with open('daily', 'w') as f:
 #       f.write(repr(daily))

#@bot.event
#async def on_message(message):
  ##  if message.content == '>daily':
  #      if (user in daily) and daily[user] > time.time():
  #          waittime = daily[id] - time.time()
  #          await message.channel.send(f'Please wait **{math.floor(waittime/3600)}h {math.floor((waittime/60) % 60)}m** to use this again!')
   #     else:
   #         d = randbelow(25001)
   #         amounts[id] =+ d
    #        await message.channel.send('You got '+ str(d) +' bunny bucks!')
    #        daily[user] = time.time() + 86400
   # save_daily()
#
#-------------------------------------------------------------------------------------------------------------------------------------- 

#@bot.command(pass_context=True)
#async def work(ctx):
#    if primary_id not in amounts: 
#        embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
#        embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
#        await ctx.send(embed=embedcoin1)
#    else:
 #       primary_id = str(ctx.message.author.id)
 #       work = randbelow(2500)
 #       embedcoin1 = discord.Embed(description=f"{ctx.author.mention} your boss payed you **" + str(work) + "** for the day^-^",color=0xFDADFD)
  #      amounts[primary_id] += work
  #      #embedcoin1.set_image(url="")
    #    await ctx.send(embed=embedcoin1)
#------------------------------------------------------------candy shop-----------------------------------------------------------------     
#shop
@bot.command(pass_context = True)
async def buycandy(ctx):
    if ctx.author.id in blacklist:
        primary_id = str(ctx.message.author.id)
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            id = str(ctx.message.author.id)
            print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the buy candy command")
            amounts[primary_id] += 100
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} do you want to buy one candy for **15k?** please answer with **yes or no**",color=0xFDADFD)
            embedcoin1.set_image(url="https://www.arcgis.com/sharing/rest/content/items/6f479a09cd6c440aa335b946b2937051/resources/1575944356705.gif")
            await ctx.send(embed=embedcoin1)
            msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
            if msg.content.lower() == "yes":
                id = str(ctx.message.author.id)
                if id not in candy:
                    if amounts[id] > 15000:
                        amounts[id] -= 15000
                        candy[id] = 0
                        embedreg1 = discord.Embed(description=f"{ctx.author.mention}<:candy8634:772148204723765259>you have baught 1 peace of candy for **15k** bunny bucks^-^<:candy8634:772148204723765259>",color=0xFDADFD)
                        embedreg1.set_image(url="https://media3.giphy.com/media/l04LqI4vxMb0Fj6lTd/giphy-downsized-large.gif")
                        candy[id] += 1
                        await ctx.send(embed=embedreg1)
                        _savecandy()
                    else:
                        embedreg1 = discord.Embed(description=f"{ctx.author.mention}<:candy8634:772148204723765259>you can not aford this transaction<:candy8634:772148204723765259>",color=0xFDADFD)
                        embedreg1.set_image(url="https://33.media.tumblr.com/5ad987ecdc9138c5980ced3a40e8dac2/tumblr_nhsxnowHiO1roi79do1_500.gif")
                        await ctx.send(embed=embedreg1)
                        _savecandy()
                else:
                    if amounts[id] > 15000:
                        candy[id] += 1
                        amounts[id] -= 15000
                        embedreg1 = discord.Embed(description=f"{ctx.author.mention}<:candy8634:772148204723765259>you have baught 1 peace of candy for **15k** bunny bucks^-^<:candy8634:772148204723765259>",color=0xFDADFD)
                        embedreg1.set_image(url="https://media3.giphy.com/media/l04LqI4vxMb0Fj6lTd/giphy-downsized-large.gif")
                        await ctx.send(embed=embedreg1)
                        _savecandy()
                    else:
                        embedreg1 = discord.Embed(description=f"{ctx.author.mention}<:candy8634:772148204723765259>you can not aford this transaction<:candy8634:772148204723765259>",color=0xFDADFD)
                        embedreg1.set_image(url="https://33.media.tumblr.com/5ad987ecdc9138c5980ced3a40e8dac2/tumblr_nhsxnowHiO1roi79do1_500.gif")
                        await ctx.send(embed=embedreg1)
                        _savecandy()
            elif msg.content.lower() == "no":
                embedreg1 = discord.Embed(description=f"{ctx.author.mention}<:candy8634:772148204723765259>*you leave the shop empty handed ^-^*<:candy8634:772148204723765259>",color=0xFDADFD)
                embedreg1.set_image(url="https://i.pinimg.com/originals/88/06/ef/8806ef6b6a79e33bcac35bf9f8358bcf.gif")
                await ctx.send(embed=embedreg1)
            else:
                await ctx.send("**OnO command timed out**")

@bot.command(pass_context=True)
async def candybalance(ctx):
    if ctx.author.id in blacklist:
        primary_id = str(ctx.message.author.id)
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the candy balance command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            id = str(ctx.message.author.id)
            if id in candy:
                embedmoney = discord.Embed(description="<:candy8634:772148204723765259>You have {} peaces of candy ^-^<:candy8634:772148204723765259>".format(candy[id]),color=0xFDADFD)
                embedmoney.set_image(url="https://data.whicdn.com/images/207609835/original.gif")
                await ctx.send(embed=embedmoney)
            else:
                embedmoney = discord.Embed(description=f"<:candy8634:772148204723765259>OnO you dont have any candy if you want to buy some candy please enter **>buycandy**<:candy8634:772148204723765259>",color=0xFDADFD)
                embedmoney.set_image(url="https://em.wattpad.com/a4c41b85710c384aa966e3af277cad0e35f87be5/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f6e6c713442616333586c473553773d3d2d3830333937393237382e313564363061393632656634643134653132313332393136373037352e676966?s=fit&w=720&h=720")
                await ctx.send(embed=embedmoney)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command(pass_context=True)
async def ping(ctx):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the ping command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            time_1 = time.perf_counter()
            await ctx.trigger_typing()
            time_2 = time.perf_counter()
            ping = round((time_2-time_1)*1000)
            await ctx.send(f"ping = {ping}ms (round trip)")
#@bot.command(pass_context=True)
#async def debuguserbunny(ctx):#fc0303
  #  l = str(ctx.message.author.id)
   # if l == "529305973576171561":
    #    if os.path.exists('amounts.json'):
   #         with open('amounts.json', 'r') as file:
   #             amounts = json.load(file)
    #    else:
   #         amounts = {}
  #      with open('amounts.json') as data_file:
   #         amounts = json.load(data_file)
  #      for element in amounts:
            #delete_id = str(ctx.message.author.id)
  #          del amounts[ctx.message.author.id]
 
 #       #with open('amounts.json', 'w+') as f:
        #    json.dump(amounts, file)
 #       #    #data[primary_id].remove(primary_id)
 #       with open('amounts.json', 'w+') as data_file:
  #          amounts = json.dump(amounts, data_file)
 #   else:
#        await ctx.send("**you do not have perms to use debug commands**")

#----------------------------------------------------------------------money------------------------------------------------------------
@bot.command(pass_context = True)
async def tweet(ctx, input):
    if ctx.author.id in blacklist:
        primary_id = str(ctx.message.author.id)
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        primary_id = str(ctx.message.author.id)
        if primary_id == "529305973576171561":#ME
            api.update_status(input)
            await ctx.send("**OwO you just tweeted: '"+input+"'**")
        elif primary_id == "245636395165548546":#KEN
            api.update_status(input)
            await ctx.send("**OwO you just tweeted: '"+input+"'**")
        else:
            id = str(ctx.message.author.id)
            print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " tryed use the tweet command")
            await ctx.send("**you do not have permission to use this command**")
#api.update_status
#------------------------------------------------------------------------------------help command-------------------------------------------------------------------------------------#
@bot.command(pass_context = True)
async def help(ctx):
    if ctx.author.id in blacklist:
        primary_id = str(ctx.message.author.id)
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the help command")
        embedhelp = discord.Embed(description=f"""list of commands ^-^:
**-new econamy commands please use the command below to see how to use them ^-^-**
**>bunnybuckscommands** ☁。lists commands for bunnys econamy
**---------------------------------------------**
**>meme** ☁。this command sends you a random wholesome meme. ^-^ 
**>recommendsong** ☁。this command gives you a kawaii music recomendation
**>stickbug** ☁。sends the user a get stick bugged meme :3
**>damedane** ☁。sends a deep fake video of isabelle from animal crossing singing dame dane (thank you to biscuit.bot on instagram for the meme ^-^)
**>hornyjail** ☁。bonks the user on the head for being the horny >:(
**>poggers** ☁。poggers in chat
**>invitelink** ☁。gives the user a invite link to add bunny to other servers ^-^
**>conga** ☁。brain go brrrrr
**>recomendgame** ☁。recomends the user a random steam game :3
**>love** ☁。sends love to another user via there @ exsample: >love @bunny#7957
**>hug** ☁。hugs another user via there @ exsample: >hug @bunny#7957
**>kiss** ☁。slaps another user via there @ exsample: >kiss @bunny#7957
**>cry** ☁。this shows the user is crying 
**>nextlaunch** ☁。shows user next rocket launch
**>homiekiss** ☁。kiss yo homie good night via there @ exsample: >homiekiss @bunny#7957
~~**>toasterbath** ☁。makes the user commit toaster bath :P.~~ **(disabled)**
**>warcrimes** ☁。makes the user commit war crimes >:3.
**>coffee** ☁。make another user a cup of coffee via there @ exsample: >coffee @bunny#7957
**>slap** ☁。slaps another user via there @ exsample: >slap @bunny#7957
**>kill** ☁。kills another user via there @ exsample: >kill @bunny#7957
**>bunnyteam** ☁。displays a message with the crdits of bunny bot ^-^
**-------------------------------------------------------------------------------**
if you guys want to help me out pay the server costs to keep bunny runing please use my paypal linked below **you dont have to donate and bunny is fully free to use! (i hate bots with premium)**
https://www.paypal.me/uwutisum""",color=0xFDADFD)
        await ctx.send(embed=embedhelp)#**tamagotchi minigame coming soon ^-^(when i mean soon i mean in like a few days lol)**
        embedhelp = discord.Embed(description=f"""**UPDATE!: new meme command changes now lets bunny use reddit, meaning no more dupe memes**""",color=0xFDADFD)
        await ctx.send(embed=embedhelp)

@bot.command(pass_context = True)
async def bunnybuckscommands(ctx):
    if ctx.author.id in blacklist:
        primary_id = str(ctx.message.author.id)
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the bunny bucks help command")
        embedbucks = discord.Embed(description=f"""<:candy2354:772148370693160980>**----------------------!BUNNY-BUCKS!----------------------**<:candy2354:772148370693160980>
**<:candy7645:772148287947669535>-how to earn bunny bucks-<:candy7645:772148287947669535>**
you earn **100** bunny bucks every time you use a command
**<:candy8634:772148204723765259>-new bunny bucks commands ^-^-<:candy8634:772148204723765259>**
**>register** ☁。registers you with the bunny bot ^-^
**>transfer** ☁。transfers a select amount of money to some one else from one bunny bank acount to another exsample: >transfer 1000 @bunny#7957 (that will transfer 1000 bunny bucks to bunnys acount)
**>cointoss** ☁。bunny will flip a coin and if it lands on heads you win double the amount you put in but if you loose you will loose the money you entered ^-^ exsample: >cointoss 1000
**---------------------candys--------------------**
candys are what you can spend you bunny bucks on they cost **15k** bunny bucks eatch ^-^ (please note as of now they dont have any benifits but i will soon be changeing that ^-^)
**>buycandy** ☁。this command lets you buy one peace of candy for **15k** bunny bucks
**>candybalance** ☁。once you get one candy you unlock the candy balance command that lets you check how many peaces of candy you have ^-^
**-----------------------------------------------**""",color=0xFDADFD)
        await ctx.send(embed=embedbucks)
#catagorys of commands ^-^:
#>commandscomingsoon ☁。
#>newcommands ☁。
#>roleplayhelp ☁。
#>econamyhelp ☁。
#>memecommandshelp ☁。
#>misccommandshelp ☁。

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-old help menu-#
#---------------#
    #author = ctx.message.author
    #embedhelp.set_author(name="help")
    #embedhelp.add_field(name=">meme", value="☁。this command sends you a random wholesome meme. ^-^", inline=False)
    #embedhelp.add_field(name=">recommendsong", value="☁。this command gives you a kawaii music recomendation", inline=False)
    #embedhelp.add_field(name=">stickbug", value="☁。sends the user a get stick bugged meme :3 ", inline=False)
    #embedhelp.add_field(name=">damedane", value="☁。sends a deep fake video of isabelle from animal crossing singing dame dane (thank you to biscuit.bot on instagram for the meme ^-^)", inline=False)
    #embedhelp.add_field(name=">hornyjail", value="☁。bonks the user on the head for being the horny >:(", inline=False)
    #embedhelp.add_field(name=">poggers", value="☁。poggers in chat", inline=False)
    #await author.send(author, embed=embedhelp)
    #await ctx.send("**please check your dms ^-^**(there is a glitch with the help menu that i am working on a fix for)")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                   ROLE PLAY COMMANDS
#   *  .  . *       *    .        .        .   *    ..
# .    *        .   ###     .      .        .            *
#    *.   *        #####   .     *      *        *    .
#  ____       *  ######### *    .  *      .        .  *   .
# /   /\  .     ###\#|#/###   ..    *    .      *  .  ..  *
#/___/  ^8/      ###\|/###  *    *            .      *   *
#|   ||%%(        # }|{  #
#|___|,  \\  ejm    }|{
#--------------------------------------------------------------------------------------warcrimes command-------------------------------------------------------------------------------#
@bot.command(pass_context = True)
async def warcrimes(ctx):
    if ctx.author.id in blacklist:
        primary_id = str(ctx.message.author.id)
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the warcrimes command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            embedwar = discord.Embed(description=f"{ctx.author.mention} Commits War crimes",color=0xFDADFD)
            embedwar.set_image(url="https://i.imgur.com/XJFqwxU.gif")
            primary_id = str(ctx.message.author.id)
            amounts[primary_id] += 100
            await ctx.send(embed=embedwar)
        _save()
#-----------------------------------------------------------------------------------------CRY COMMAND----------------------------------------------------------------------------------#
@bot.command(pass_context = True)
async def cry(ctx):
    if ctx.author.id in blacklist:
        primary_id = str(ctx.message.author.id)
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the cry command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            embedcry = discord.Embed(description=f"{ctx.author.mention} Crys ;A;",color=0xFDADFD)
            c = (randbelow(2))
            if c == 0:
                embedcry.set_image(url="https://66.media.tumblr.com/48bdc1aebf0531598b4cd51be7701a45/tumblr_o349ccKT9C1slmfozo1_540.gif")
                await ctx.send(embed=embedcry)
            elif c == 1:
                embedcry.set_image(url="https://38.media.tumblr.com/6ecacbb69194f280a98ec5b52af54adc/tumblr_nk4kui4YGF1uo1owvo1_500.gif")
                await ctx.send(embed=embedcry)
        _save()
#------------------------------------------------------------------------toaster bath command------------------------------------------------------------------------------#
#fuck top.gg all my homies fucking hate top.gg
@bot.command(pass_context = True)
async def toasterbath(ctx):
    primary_id = str(ctx.message.author.id)
    if primary_id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        if primary_id == "529305973576171561":#ME
            embedbath = discord.Embed(description=f"{ctx.author.mention} Commits Toaster Bath",color=0xFDADFD)
            embedbath.set_image(url="https://pics.me.me/lets-take-a-bath-oni-chan-commit-toaster-bath-39891287.png")
            await ctx.send(embed=embedbath)
        elif primary_id == "245636395165548546":#KEN
            embedbath = discord.Embed(description=f"{ctx.author.mention} Commits Toaster Bath",color=0xFDADFD)
            embedbath.set_image(url="https://pics.me.me/lets-take-a-bath-oni-chan-commit-toaster-bath-39891287.png")
            await ctx.send(embed=embedbath)
        else:
            id = str(ctx.message.author.id)
            print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " tryed to use the toaster bath command")
            await ctx.send("**this command has been removed from bunny**")
        _save()
#------------------------------------------------------------------------bunny team command------------------------------------------------------------------------------------#
@bot.command(pass_context = True)
async def bunnyteam(ctx):
    primary_id = str(ctx.message.author.id)
    if primary_id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            id = str(ctx.message.author.id)
            print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the bunny team command")
            embedteam = discord.Embed(description=f"""**Bunny bot team ^-^**
-----------------------------------------------
*Kenorai bunnys lead artist*
-----------------------------------------------
*UwUtisum bunnys lead programer and owner of bunny bot ^-^*
-----------------------------------------------
*peyton bunnys test dummy/beta tester*
-----------------------------------------------""",color=0xFDADFD)
            await ctx.send(embed=embedteam)
#------------------------------------------------------------------------slap command------------------------------------------------------------------------------------#
@bot.command(pass_context = True)
async def slap(ctx, other: discord.Member):#https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTdAvQXXE-KkVDQqig5jKQXCn8LsRJz4CXNFw&usqp=CAU
    primary_id = str(ctx.message.author.id)
    if primary_id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the slap command")
        other_id = str(other.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        elif other_id == primary_id:
            amounts[primary_id] += 100
            embedslap = discord.Embed(description=f"{ctx.author.mention} Slaps them self",color=0xFDADFD)
            embedslap.set_image(url="http://media.giphy.com/media/Zau0yrl17uzdK/giphy.gif")
            await ctx.send(embed=embedslap)
        else:
            amounts[primary_id] += 100
            embedslap = discord.Embed(description=f"{ctx.author.mention} Slaps {other.mention}",color=0xFDADFD)
            embedslap.set_image(url="http://media.giphy.com/media/Zau0yrl17uzdK/giphy.gif")
            await ctx.send(embed=embedslap)
        _save()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command(pass_context = True)
async def love(ctx, other: discord.Member):
    if ctx.author.id in blacklist:
        primary_id = str(ctx.message.author.id)
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the love command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            embedslap = discord.Embed(description=f"{ctx.author.mention} gives love to {other.mention}",color=0xFDADFD)
            embedslap.set_image(url="https://i.gifer.com/6Sam.gif")
            await ctx.send(embed=embedslap)
        _save()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command(pass_context = True)
async def homiekiss(ctx, other: discord.Member):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the homie kiss command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            embedslap = discord.Embed(description=f"{ctx.author.mention} kisses their homie {other.mention}",color=0xFDADFD)
            embedslap.set_image(url="https://j.gifs.com/oV75rz.gif")
            await ctx.send(embed=embedslap)
        _save()

@bot.command(pass_context = True)
async def coffee(ctx, other: discord.Member):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the coffee command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            embedslap = discord.Embed(description=f"{ctx.author.mention} makes a cup of coffee for {other.mention}",color=0xFDADFD)
            embedslap.set_image(url="https://i.pinimg.com/originals/d2/42/c8/d242c8d9b88b5ffa04d2a3e50f3b49f3.gif")
            await ctx.send(embed=embedslap)
        _save()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

@bot.command(pass_context = True)
async def kill(ctx, other: discord.Member):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the kill command")
        other_id = str(other.id)
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        elif other_id == primary_id:
            embedslap = discord.Embed(description=f"if you are felling depressed lonely or sad remember that there are tones of pepole around you that love you and care for you even if you think there isnt i bet you there is someone out there that loves you to bits doing this is never the way to fix things if you want to talk to some one you can call the samaritans 24h hotline **(116 123)** where you can have a chat and they can help you get back on the right path",color=0xFDADFD)
            embedslap.set_image(url="https://i.imgur.com/r9aU2xv.gif?noredirect")
            await ctx.send(embed=embedslap)
        else:
            amounts[primary_id] += 100
            embedslap = discord.Embed(description=f"{ctx.author.mention} kill's {other.mention}",color=0xFDADFD)
            embedslap.set_image(url="https://media1.tenor.com/images/e4db2e0888c2c85a042ea9e54fc4d771/tenor.gif?itemid=16079109")
            await ctx.send(embed=embedslap)
        _save()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

@bot.command(pass_context = True)
async def hug(ctx, other: discord.Member):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the hug command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            embedslap = discord.Embed(description=f"{ctx.author.mention} hugs {other.mention}",color=0xFDADFD)
            embedslap.set_image(url="https://25.media.tumblr.com/tumblr_ma7l17EWnk1rq65rlo1_500.gif")
            await ctx.send(embed=embedslap)
        _save()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
@bot.command(pass_context = True)
async def kiss(ctx, other: discord.Member):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the kiss command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            embedslap = discord.Embed(description=f"{ctx.author.mention} kisses {other.mention}",color=0xFDADFD)
            embedslap.set_image(url="https://i.pinimg.com/originals/40/37/e6/4037e6ae03275bd33b3e5df50acda41a.gif")
            await ctx.send(embed=embedslap)
        _save()
@bot.command(pass_context = True)
async def servernum(ctx):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used ther server num command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            await ctx.send("I'm in " + str(len(bot.guilds)) + " servers!")
        _save()

@bot.command(pass_context = True)
async def conga(ctx):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the conga command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            await ctx.send("**my brain go brrrrrrr**\nhttps://matias.ma/nsfw/")
        _save()

@bot.command(pass_context = True)
async def invitelink(ctx):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " got the invite link for bunny")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            await ctx.send("**here is a invite link for bunnybot ^-^** \n https://discord.com/api/oauth2/authorize?client_id=741998827933794396&permissions=8&scope=bot")#**here is a invite link for bunnybot ^-^** \n https://discord.com/api/oauth2/authorize?client_id=741998827933794396&permissions=8&scope=bot
        _save()

@bot.command(pass_context = True)
async def hornyjail(ctx):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the horny jail command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            await ctx.send("**BONK!** go to horny jail >:(")
        _save()

@bot.command(pass_context = True)
async def secret(ctx):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the secret command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            await ctx.send(".- .... .-. ----- -.-. .... -- -.... .-.. -.-- ----. ..... -... ...-- ...- ----- -.. ... ..... .. --.. ... ----. -.- ..- -..- -.-. ----- -.. --.. .-.. -..- --.. .---- .... .--- ..- --.- -...- -...- / -.--. - .... .. ... / .. ... / .- / -... .- ... . / -.... ....- / -.-. --- -.. . -.--.-")
        _save()
@bot.command(pass_context = True)
async def damedane(ctx):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the damedane command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            await ctx.send("https://youtu.be/H_cEvZg2DDc")
        _save()

@bot.command(pass_context = True)
async def  stickbug(ctx):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the stickbug command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            embed.set_image(url="https://i.imgur.com/WW9VN8I.gif")
            await ctx.send(embed=embed)
        _save()

@bot.command(pass_context = True)
async def  poggers(ctx):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " said poggers in chat")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            await ctx.send("**POGGERS IN CHAT! :0**")
        _save()
        
@bot.command(pass_context=True)
async def leah(ctx):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the leah command")
        primary_id = str(ctx.message.author.id)
        if primary_id == "529305973576171561":
            await ctx.send("**OWO is that my creator the all mighty leah!**")
        else:
            await ctx.send("**YOUR NOT LEAH!**")
#-----------------------------------------------------------------------------------------------------------------------------------------------
@bot.command(pass_context=True)
async def bunnypem(ctx):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        primary_id = str(ctx.message.author.id)
        if primary_id == "529305973576171561":
            await ctx.send(""" """) #REMOVED 
        else:
            return
#---------------------------------------------------------------------------------------------------------------------------------------------
@bot.command(pass_context=True)
async def ken(ctx):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used ken command")
        primary_id = str(ctx.message.author.id)
        if primary_id == "245636395165548546":
            await ctx.send("**OWO is that my lead artist KenKen**")
        else:
            await ctx.send("**YOUR NOT KEN**")

@bot.command(pass_context = True)
async def recommendgame(ctx):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used recommend game command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            g = (randbelow(17))
            if g == 0:
                await ctx.send("https://store.steampowered.com/app/739630/Phasmophobia/")
            elif g == 1:
                await ctx.send("https://store.steampowered.com/app/1139900/Ghostrunner/")
            elif g == 2:
                await ctx.send("https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/")
            elif g == 3:
                await ctx.send("https://store.steampowered.com/app/578650/The_Outer_Worlds/")
            elif g == 4:
                await ctx.send("https://store.steampowered.com/app/1097150/Fall_Guys_Ultimate_Knockout/")
            elif g == 5:
                await ctx.send("https://store.steampowered.com/app/275850/No_Mans_Sky/")
            elif g == 6:
                await ctx.send("https://store.steampowered.com/app/1250410/Microsoft_Flight_Simulator/")
            elif g == 7:
                await ctx.send("https://store.steampowered.com/app/264710/Subnautica/")
            elif g == 8:
                await ctx.send("https://store.steampowered.com/app/220200/Kerbal_Space_Program/")
            elif g == 9:
                await ctx.send("https://store.steampowered.com/app/782330/DOOM_Eternal/")
            elif g == 10:
                await ctx.send("https://store.steampowered.com/app/746850/Cloudpunk/")
            elif g == 11:
                await ctx.send("https://store.steampowered.com/app/438100/VRChat/")
            elif g == 12:
                await ctx.send("https://store.steampowered.com/app/284160/BeamNGdrive/")
            elif g == 13:
                await ctx.send("https://store.steampowered.com/app/613100/House_Flipper/")
            elif g == 14:
                await ctx.send("https://store.steampowered.com/app/573090/Stormworks_Build_and_Rescue/")
            elif g == 15:
                await ctx.send("https://store.steampowered.com/app/621060/PC_Building_Simulator/")
            elif g == 16:
                await ctx.send("https://store.steampowered.com/app/504230/Celeste/")
        _save()

##@bot.command(pass_context = True)
#async def match(ctx other: discord.Member):
 #   if ctx.author.id in blacklist:
 #       await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
 #   else:
   #     primary_id = str(ctx.message.author.id)
  #      if primary_id not in amounts: 
   #         embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
  #          embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
   #         await ctx.send(embed=embedcoin1)
  #      else:

@bot.command(pass_context = True)
async def recommendsong(ctx):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used recommend song command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            y = (randbelow(94))
            if y == 0:
                await ctx.send("https://www.youtube.com/watch?v=_QfPliSW83A&feature=share")
            elif y == 1:
                await ctx.send("https://www.youtube.com/watch?v=UCcGuJzewCo&feature=share")
            elif y == 2:
                await ctx.send("https://www.youtube.com/watch?v=AufydOsiD6M&feature=share")
            elif y == 3:
                await ctx.send("https://www.youtube.com/watch?v=uKDuIhNVLyg&feature=share")
            elif y == 4:
                await ctx.send("https://www.youtube.com/watch?v=YNlRsv7aCOw&feature=share")
            elif y == 5:
                await ctx.send("https://www.youtube.com/watch?v=f3RVootcD4w&feature=share")
            elif y == 6:
                await ctx.send("https://www.youtube.com/watch?v=6kPHNW8kdcs&feature=share")
            elif y == 7:
                await ctx.send("https://www.youtube.com/watch?v=meCqh5leHrQ&feature=share")
            elif y == 8:
                await ctx.send("https://www.youtube.com/watch?v=uKxyLmbOc0Q&feature=share")
            elif y == 9:
                await ctx.send("https://www.youtube.com/watch?v=pcw-JItoL1U&feature=share")
            elif y == 10:
                await ctx.send("https://www.youtube.com/watch?v=7PYe57MwxPI&feature=share")
            elif y == 11:
                await ctx.send("https://www.youtube.com/watch?v=tdi19AZvHkQ&feature=share")
            elif y == 12:
                await ctx.send("https://www.youtube.com/watch?v=I-QmZpLWjHc&feature=share")
            elif y == 13:
                await ctx.send("https://www.youtube.com/watch?v=S8dmq5YIUoc&feature=share")
            elif y == 14:
                await ctx.send("https://www.youtube.com/watch?v=3w-C0-zVaW8&feature=share")
            elif y == 15:
                await ctx.send("https://www.youtube.com/watch?v=ZALu6OJwAKs&feature=share")
            elif y == 16:
                await ctx.send("https://www.youtube.com/watch?v=oMUBHzCZwZo&feature=share")
            elif y == 17:
                await ctx.send("https://www.youtube.com/watch?v=sBl3EpUqAjE&feature=share")
            elif y == 18:
                await ctx.send("https://www.youtube.com/watch?v=4eaXoebXKfY&feature=share")
            elif y == 19:
                await ctx.send("https://www.youtube.com/watch?v=p_hdmt4vpBo&feature=share")
            elif y == 20:
                await ctx.send("https://www.youtube.com/watch?v=b5Km0KQ2ojo&feature=share")
            elif y == 21:
                await ctx.send("https://www.youtube.com/watch?v=Ni0bXuKvvT8&feature=share")
            elif y == 22:
                await ctx.send("https://www.youtube.com/watch?v=SmKKG6tCP3M&feature=share")
            elif y == 23:
                await ctx.send("https://www.youtube.com/watch?v=RKtoreimcQ8&feature=share")
            elif y == 24:
                await ctx.send("https://www.youtube.com/watch?v=oHua-5bb43o&feature=share")
            elif y == 25:
                await ctx.send("https://www.youtube.com/watch?v=jkTvY8ZLZ-g&feature=share")
            elif y == 26:
                await ctx.send("https://www.youtube.com/watch?v=UtF6Jej8yb4&feature=share")
            elif y == 27:
                await ctx.send("https://www.youtube.com/watch?v=FTQbiNvZqaY&feature=share")
            elif y == 28:
                await ctx.send("https://www.youtube.com/watch?v=sAKoLFfhoCg&feature=share")
            elif y == 29:
                await ctx.send("https://www.youtube.com/watch?v=SQTcRxPsoMo&feature=share")
            elif y == 30:
                await ctx.send("https://www.youtube.com/watch?v=FU-9kt-qi1g&feature=share")
            elif y == 31:
                await ctx.send("https://www.youtube.com/watch?v=NocXEwsJGOQ&feature=share")
            elif y == 32:
                await ctx.send("https://www.youtube.com/watch?v=_I6I2JOJhHY&feature=share")
            elif y == 33:
                await ctx.send("https://www.youtube.com/watch?v=pXRviuL6vMY&feature=share")
            elif y == 34:
                await ctx.send("https://www.youtube.com/watch?v=zxbufWzX1NA&feature=share")
            elif y == 35:
                await ctx.send("https://www.youtube.com/watch?v=VYaygLi1Qd0&feature=share")
            elif y == 36:
                await ctx.send("https://www.youtube.com/watch?v=1G4isv_Fylg&feature=share")
            elif y == 37:
                await ctx.send("https://www.youtube.com/watch?v=zhIScvlFn2w&feature=share")
            elif y == 38:
                await ctx.send("https://www.youtube.com/watch?v=ktvTqknDobU&feature=share")
            elif y == 39:
                await ctx.send("https://www.youtube.com/watch?v=yL4eIUTovLM&feature=share")
            elif y == 40:
                await ctx.send("https://www.youtube.com/watch?v=Sv6dMFF_yts&feature=share")
            elif y == 41:
                await ctx.send("https://www.youtube.com/watch?v=uuBETyA_yxc&feature=share")
            elif y == 42:
                await ctx.send("https://www.youtube.com/watch?v=UprcpdwuwCg&feature=share")
            elif y == 43:
                await ctx.send("https://www.youtube.com/watch?v=2rn-vMbFglI&feature=share")
            elif y == 44:
                await ctx.send("https://www.youtube.com/watch?v=gl7zqpZBVrc&feature=share")
            elif y == 45:
                await ctx.send("https://www.youtube.com/watch?v=qTsaS1Tm-Ic&feature=share")
            elif y == 46:
                await ctx.send("https://www.youtube.com/watch?v=Io0fBr1XBUA&feature=share")
            elif y == 47:
                await ctx.send("https://www.youtube.com/watch?v=yLrstz80MKs&feature=share")
            elif y == 48:
                await ctx.send("https://www.youtube.com/watch?v=225K-LR62Ek&feature=share")
            elif y == 49:
                await ctx.send("https://www.youtube.com/watch?v=O-MQC_G9jTU&feature=share")
            elif y == 50:
                await ctx.send("https://www.youtube.com/watch?v=YNm3Ggv01Ns&feature=share")
            elif y == 51:
                await ctx.send("https://www.youtube.com/watch?v=QzcvRDWgRIE&feature=share")
            elif y == 52:
                await ctx.send("https://www.youtube.com/watch?v=ele2DMU49Jk&feature=share")
            elif y == 53:
                await ctx.send("https://www.youtube.com/watch?v=p1YH7dec2i0&feature=share")
            elif y == 54:
                await ctx.send("https://www.youtube.com/watch?v=UOxkGD8qRB4&feature=share")
            elif y == 55:
                await ctx.send("https://www.youtube.com/watch?v=yPYZpwSpKmA&feature=share")
            elif y == 56:
                await ctx.send("https://www.youtube.com/watch?v=bpOSxM0rNPM&feature=share")
            elif y == 57:
                await ctx.send("https://www.youtube.com/watch?v=gykWYPrArbY&feature=share")
            elif y == 58:
                await ctx.send("https://www.youtube.com/watch?v=cL4o31W5sEk&feature=share")
            elif y == 59:
                await ctx.send("https://www.youtube.com/watch?v=VMHo1nLX1ek&feature=share")
            elif y == 60:
                await ctx.send("https://www.youtube.com/watch?v=kH-5SRKsj8E&feature=share")
            elif y == 61:
                await ctx.send("https://www.youtube.com/watch?v=su0FCBRwVpE&feature=share")
            elif y == 62:
                await ctx.send("https://www.youtube.com/watch?v=h9wualcJuE4&feature=share")
            elif y == 63:
                await ctx.send("https://www.youtube.com/watch?v=DhHGDOgjie4&feature=share")
            elif y == 64:
                await ctx.send("https://www.youtube.com/watch?v=qLufwxIfQWg&feature=share")
            elif y == 65:
                await ctx.send("https://www.youtube.com/watch?v=VHb_XIql_gU&feature=share")
            elif y == 66:
                await ctx.send("https://www.youtube.com/watch?v=4hdKXr8wGrk&feature=share")
            elif y == 67:
                await ctx.send("https://www.youtube.com/watch?v=feq6MOg3qpA&feature=share")
            elif y == 68:
                await ctx.send("https://www.youtube.com/watch?v=4A4ZiZwPejY&feature=share")
            elif y == 69:
                await ctx.send("https://www.youtube.com/watch?v=TWb01hPJjA8&feature=share")
            elif y == 70:
                await ctx.send("https://www.youtube.com/watch?v=WqCpWu8tgRw&feature=share")
            elif y == 71:
                await ctx.send("https://www.youtube.com/watch?v=o_TIdWRuixo&feature=share")
            elif y == 72:
                await ctx.send("https://www.youtube.com/watch?v=p00v9ZFhWJM&feature=share")
            elif y == 73:
                await ctx.send("https://www.youtube.com/watch?v=RQmEERvqq70&feature=share")
            elif y == 74:
                await ctx.send("https://www.youtube.com/watch?v=3a-q7vPa-UU&feature=share")
            elif y == 75:
                await ctx.send("https://www.youtube.com/watch?v=U-Ooxpz0Eqk&feature=share")
            elif y == 76:
                await ctx.send("https://www.youtube.com/watch?v=HZIdqqVfZD4&feature=share")
            elif y == 77:
                await ctx.send("https://www.youtube.com/watch?v=wOjcOIYGaOc&feature=share")
            elif y == 78:
                await ctx.send("https://www.youtube.com/watch?v=Eif5IUfejV0&feature=share")
            elif y == 79:
                await ctx.send("https://www.youtube.com/watch?v=QL9_rPPyCMQ&feature=share")
            elif y == 80:
                await ctx.send("https://www.youtube.com/watch?v=2SM_A6Wmx2I&feature=share")
            elif y == 81:
                await ctx.send("https://www.youtube.com/watch?v=dCrLMwDz5qE&feature=share")
            elif y == 82:
                await ctx.send("https://www.youtube.com/watch?v=ezfqeIWXT2I&feature=share")
            elif y == 83:
                await ctx.send("https://www.youtube.com/watch?v=EHyoAXILbA8&feature=share")
            elif y == 84:
                await ctx.send("https://www.youtube.com/watch?v=jhl5afLEKdo&feature=share \nthe real miku anthem")
            elif y == 85:
                await ctx.send("https://www.youtube.com/watch?v=0tPRHqGPL8I&feature=share")
            elif y == 86:
                await ctx.send("https://www.youtube.com/watch?v=bqSnxyQje5M&feature=share")
            elif y == 87:
                await ctx.send("https://www.youtube.com/watch?v=3nlSDxvt6JU&feature=share")
            elif y == 88:
                await ctx.send("https://www.youtube.com/watch?v=JVovZkcU5tk&feature=share")
            elif y == 89:
                await ctx.send("https://www.youtube.com/watch?v=ZsMb66Lb9Sc&feature=share")
            elif y == 90:
                await ctx.send("https://www.youtube.com/watch?v=NpkDLCo8O8k&feature=share")
            elif y == 91:
                await ctx.send("https://www.youtube.com/watch?v=i-gA0vcBnPI&feature=share")
            elif y == 92:
                await ctx.send("https://www.youtube.com/watch?v=tQpKb0U800I&feature=share")
            elif y == 93:
                await ctx.send("https://www.youtube.com/watch?v=OLpeX4RRo28&feature=share")
            else:
                print("(music)error at :", + (y))
            _save()

@bot.command(pass_context=True)
async def meme(ctx):
    if ctx.author.id in blacklist:
        await ctx.send("**Oopsie Woopsie Uwu We made a fucko boingo! The code monkeys awer working VEWY HAWD to fix this!**")
        print("["+ Fore.RED + "BLOCKED" + Style.RESET_ALL + "] " + Fore.YELLOW + str(primary_id) + " Tried to use bunny" +Style.RESET_ALL)
    else:
        id = str(ctx.message.author.id)
        print("["+ Fore.GREEN + 'Sent' + Style.RESET_ALL + "] " + Fore.YELLOW + str(id) + Style.RESET_ALL + " used the meme command")
        primary_id = str(ctx.message.author.id)
        if primary_id not in amounts: 
            embedcoin1 = discord.Embed(description=f"{ctx.author.mention} You do not have an account please enter **>register** to create an account with bunnybot ^-^",color=0xFDADFD)
            embedcoin1.set_image(url="https://68.media.tumblr.com/c51e2d9edd060cd45c18aec6a150e7b6/tumblr_nxtaijRCSu1trpnp2o1_500.gif")
            await ctx.send(embed=embedcoin1)
        else:
            amounts[primary_id] += 100
            reddit = asyncpraw.Reddit(client_id='',#REMOVED 
                            client_secret='', #REMOVED 
                            password="", #REMOVED 
                            user_agent='',#REMOVED 
                            username='')#REMOVED 

            message = await ctx.send("Looking for memes...")
            await asyncio.sleep(1)
            await message.edit(content="Found one for you ^-^:")
            subreddit = await reddit.subreddit("wholesomememes")
            all_subs = []
            top = subreddit.hot(limit=200)
            async for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            em =  discord.Embed(title=name,color=0xFDADFD)
            em.set_image(url=url)
            em.set_footer(text="Data from /r/Wholesomememes on Reddit")
            await message.edit(embed=em)
            _save()

@bot.command()
async def save():
    _save()

@bot.command()
async def savecandy():
    _savecandy()

@bot.command()
async def savepets():
    _savepets()

bot.run("")#REMOVED 
