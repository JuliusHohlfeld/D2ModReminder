bot_token = "OTgwNTMyMTc2MzUxMjc3MTA2.GaikZP.ycEP6d8CdBv5EAsbTUg5zsnXsPhDvKGLOb_lEk"

import os
import requests
import json

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
API_KEY = os.getenv('X_API_KEY')
ENDPOINT = os.getenv('BUNGIE_ENDPOINT')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

bot = commands.Bot(command_prefix='!')

@bot.command(name='register', help="Allow the bot to view your inventory. You must add your Bungie Name und Number Code to the command.")
async def register(ctx, bungie_name, bungie_code):
    session = requests.Session()
    session.headers.update({"X-API-Key": API_KEY})

    url = ENDPOINT+"/Destiny2/SearchDestinyPlayerByBungieName/All/" 
    payload = {"displayName": str(bungie_name), "displayNameCode": bungie_code}
    payload = json.dumps(payload)
    #we now have information requiered to look at the profile of the player
    api_response = session.post(url, data=payload)
    user = json.loads(api_response.content)

    user = user.get("Response")
    member_type = user[0]['membershipType']
    member_id = user[0]['membershipId']
    url = ENDPOINT+"/Destiny2/"+str(member_type)+"/Profile/"+str(member_id)+"/?components=800"
    print(url)
    profile_response = session.get(url)

    bot_response = """Welcome """ + str(bungie_name) + "#" + str(bungie_code) + """!
    Please grant D2 Mod Reminder the right to view the inventory of your Destiny 2 characters.
    Follow this link: gibberish"""
    await ctx.send(bot_response)
    print(profile_response.content)
    collect_ada_mods(member_id,member_type, session)

@bot.command(name='today', help='The bot shows you the currently available combat style mods in Ada-1\'s inventory.')
async def today(ctx):
    session = requests.Session()
    session.headers.update({"X-API-Key": API_KEY})

    collect_ada_mods(0,0, 0, session)
    return

def get_any_character(profile_content):
    return

def collect_ada_mods(character_id, member_id, member_type, session):
    # url = ENDPOINT + "?characterId=" + character_id 
    # url += "&destinyMembershipId="+member_id+"&membershipType="+member_type
    # url += "&vendorHash=350061650&components=401"

    url = ENDPOINT + "/Destiny2/Manifest/DestinyVendorDefinition/350061650"
    print(url)
    response = session.get(url)
    print(response.content)
    return

bot.run(TOKEN)