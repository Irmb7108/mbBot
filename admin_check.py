# from pyrogram.enums import ChatMemberStatus
# from pyrogram.types import Message
# import asyncio
# from pyrogram.client import bot
# async def admin_check(client, msg):
#     userid = msg.from_user.id
#     grp_id = msg.chat.id
#     admins = await bot.get_chat_member(grp_id, userid)
#     if admins.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
#         pass
#         await msg.reply(f"is don")
#         return True
#     elif admins.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
#         await msg.reply(f" not admins ")
#         return False
#     else:
#         await bot.reply("command not filnd")

from pyrogram.types import Message
from pyrogram.client import bot
from pyrogram import Client, filters
from pyrohelpers import extract_user
async def admin_check(message: Message) -> bool:
    if not message.from_user:
        return False

    if message.chat.type not in ["supergroup", "channel"]:
        return False

    if message.from_user.id in [
        777000,  # Telegram Service Notifications
        1087968824  # GroupAnonymousBot
    ]:
        return True

    client = message._client
    chat_id = message.chat.id
    user_id = message.from_user.id

    check_status = await client.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )
    admin_strings = [
        "creator",
        "administrator"
    ]
    # https://git.colinshark.de/PyroBot/PyroBot/src/branch/master/pyrobot/modules/admin.py#L69
    if check_status.status not in admin_strings:
        return False
    else:
        return True