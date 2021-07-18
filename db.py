import discord
from discord.ext import commands
import pyrebase
from json import loads , load 

with open("firebase.json", "r") as read_file:
    firebase = pyrebase.initialize_app(load(read_file))
db = firebase.database()

"""
How user Data will be stored in database?

Guild_Var:
    <guild> : [key]
        Prefix : str
        todoChannel : int
"""
def new_guild(guild_id: int):
    db.child("Guild_Var").child(guild_id).set(
        {"prefix":'amy ', "todochannel":0})

# Add prefix in Database
def add_prefix(guild_id: int, prefix: str):
    guild_prefix = db.child("Guild_Var").child(guild_id).get().val()
    if guild_prefix == None:
        new_guild(guild_id)
    guild_prefix["prefix"] = prefix
    db.child("Guild_Var").child(guild_id).set(guild_prefix)

# Check prefix 
def check_prefix(guild_id: int):
    guild_prefix = db.child("Guild_Var").child(guild_id).get().val()
    if guild_prefix == None:
        new_guild(guild_id)
        guild_prefix = db.child("Guild_Var").child(guild_id).get().val()
    prefix = str(guild_prefix["prefix"])
    return prefix