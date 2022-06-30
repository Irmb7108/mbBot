"""
Banning and kicking module

Usage:
**/kick**
To kick a member (without banning). Reply to user or have their username or id as the argument
**/ban**
To ban a member. Reply to user or have their username or id as the argument.
Enter a multiple of **s, m, h, d, w, M or y**(e.g. 2M for 2 months) as the last argument to specify the amount of time the user will be banned for. The minimum is 30 seconds and the maximum is 366 days. If the time specified is not in this range they will be banned forever
**/unban**
To unban a member. Reply to user or have their username or id as the argument
"""
# import time
# from os import environ
# from pyrogram.client import bot
# from pyrogram import errors, filters

# from ..shutup import app, bot_username, getFullName, owner_id
from os import environ

from pyrogram import errors
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message
import asyncio
from pyrogram.client import bot
timePeriods = dict(zip(['s', 'm', 'h', 'd', 'w', 'M', 'y'], [('second', 1), ('minute', 60), (
    "hour", 3600), ("day", 86400), ("week", 86400*7), ("month", 86400*30), ("year", 86400*365)]))
owner_id = int(environ["1259219363"])
bot_username = environ["Atreg006bot"]
def getFullName(user):
    return " ".join([user.first_name if user.first_name else "", user.last_name if user.last_name else ""]).strip()

@bot.on_message(filters.command(["kick", f"kick@{bot_username}"]))
async def kick(client, message):
    if(not (await message.chat.get_member("self")).can_restrict_members):
        await message.reply_text("I need additional permissions to restrict users")
        return
    if(message.reply_to_message):
        effectiveId = message.reply_to_message.from_user.id
    elif(len(message.command) > 1):
        effectiveId = message.command[1]
    else:
        await message.reply_text(
            "No user specified. Reply to the user or have their id as the argument")
        return
    if((await message.chat.get_member(message.from_user.id)).can_restrict_members or message.from_user.id == owner_id):
        try:
            await message.chat.kick_member(effectiveId)
        except errors.exceptions.bad_request_400.UserAdminInvalid:
            await message.reply_text("This user is an admin")
            return
        await message.chat.unban_member(effectiveId)
        await message.reply_text(
            f"Kicked {getFullName(await bot.get_users(effectiveId))}")
    else:
        await message.reply_text(
            "You must have user restricting permissions to use this command")



@bot.on_message(filters.command(["unban", f"unban@{bot_username}"]))
async def unban(client, message):
    if(not (await message.chat.get_member("self")).can_restrict_members):
        await message.reply_text("I need additional permissions to restrict users")
        return
    if(message.reply_to_message):
        effectiveId = message.reply_to_message.from_user.id
    elif(len(message.command) > 1):
        effectiveId = message.command[1]
    else:
        await message.reply_text(
            "No user specified. Reply to the user or have their id as the argument")
        return
    if((await message.chat.get_member(message.from_user.id)).can_restrict_members or message.from_user.id == owner_id):
        await message.chat.unban_member(effectiveId)
        await message.reply_text(
            f"Unbanned {getFullName(await bot.get_users(effectiveId))}")
    else:
        await message.reply_text(
            "You must have user restricting permissions to use this command")
