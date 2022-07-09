import base64
import os
import urllib
from datetime import datetime, timedelta
from os import getenv
from cast import *
import requests
from pyromod import listen
import asyncio
from time import sleep, time
import time
from pyrogram import*
from pyrogram import Client, filters, enums, errors
from pyrogram.raw.functions.messages import UpdatePinnedMessage
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, update, User, ChatPermissions,ChatMemberUpdated
from translation import Translation
#from pyrohelpers import extract_user,get
from os import environ
from pyrogram.enums import ChatMemberStatus as CMS, ChatMembersFilter, ChatMemberStatus
from pyrogram.errors import *
import admin_check
from parser import mention_markdown
import encode_string
import json
from pyrohelpers import  * #extract_user ,get_file_id,last_online
bot= Client(
    "my_account",
    api_id="", api_hash="",

    bot_token=""
)

owner_id = int("1259219363")
bot_username = "Atreg006bot"
def getFullName(user):
    return " ".join([user.first_name if user.first_name else "", user.last_name if user.last_name else ""]).strip()

@bot.on_message(filters.new_chat_members)
async def auto_welcome(bot: bot, msg: Message):
    # first = msg.from_user.first_name
    # last = msg.from_user.last_name
    # mention = msg.from_user.mention
    # username = msg.from_user.username
    id = msg.from_user.id
    useradd = msg.new_chat_members[0].mention
    iduser =  msg.new_chat_members[0].id
    group_name = msg.chat.title
    group_username = msg.chat.username
    name_button = "🔰 JOIN NOW 🔰"
    link_button = "t.me/bodyguard_ch"
    button_name = os.environ.get("WELCOME_BUTTON_NAME", name_button)
    button_link = os.environ.get("WELCOME_BUTTON_LINK", link_button)
    welcome_text = f"""Hey {useradd} Welcome To **{group_name}**  id: `{iduser}`
date : {msg.date}"""
#     WELCOME_TEXT = os.environ.get("WELCOME_TEXT", welcome_text)
#     # print("Welcome Message Activate")
#     BUTTON = bool(os.environ.get("WELCOME_BUTTON"))
# #     # if not BUTTON:
# #
#     # # else:
    await msg.reply_text(welcome_text)
#
START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('⚙️ Help', callback_data='help'),
            InlineKeyboardButton('About 🔰', callback_data='about'),
            InlineKeyboardButton('Close ✖️', callback_data='close')
        ]
    ]
)

buttons = [[
    InlineKeyboardButton('➕ 𝗮𝗱𝗱 𝗰𝗵𝗮𝘁 ➕', url=f'http://t.me/@Noruto321_bot?startgroup=true')
], [
    InlineKeyboardButton('🤠 𝗵𝗲𝗹𝗽 🤠', callback_data='help'),
    InlineKeyboardButton('🤓 𝗮𝗯𝗼𝘂𝘁 🤓', callback_data='about')
], [
    InlineKeyboardButton('🔎 𝘀𝗲𝗮𝗿𝗰𝗵 🔍', switch_inline_query_current_chat='')
], [
    InlineKeyboardButton('👨‍💻 𝘀𝘂𝗽𝗽𝗼𝗿𝘁 👩‍💻', url='https://t.me/movie_bus6')
], [
    InlineKeyboardButton('🤠 𝘆𝗼𝘂 𝘁𝘂𝗯𝗲 🤠', url='https://youtube.com/channel/UCVbKgUOGVEdQlmLJ_fXrWMQ')
], [
    InlineKeyboardButton('🤐 𝗰𝗹𝗼𝘀𝗲 🤐', callback_data='close_data')
]]
HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('🏘 Home', callback_data='home'),
            InlineKeyboardButton('About 🔰', callback_data='about'),
            InlineKeyboardButton('Close ✖️', callback_data='close')
        ]
    ]
)

ABOUT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('🏘 Home', callback_data='home'),
            InlineKeyboardButton('Help ⚙️', callback_data='help'),
            InlineKeyboardButton('Close ✖️', callback_data='close')
        ]
    ]
)

HELP_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("Telegram id", callback_data="id"),
       InlineKeyboardButton("Telegram info ", callback_data="info")
       ]]
)
class Translation(object):
    ABOUT = """
    📝 Language: Python 3
    🧰 Framework: Pyrogram
    👨‍💻 Developer: [Anonymous](https://t.me/ir_mb)
    📮 Channel: [کانال ربات بادیگارد](https://t.me/Bodyguard_Ch)
    👥 Group: [گروه پشتیبانی ربات ](https://t.me/Bodyguard_Ch)
    """
    back = "welcom"

    buttons = [[
        InlineKeyboardButton('➕ 𝗮𝗱𝗱 𝗰𝗵𝗮𝘁 ➕', url=f'http://t.me/@Noruto321_bot?startgroup=true')
    ], [
        InlineKeyboardButton('🤠 𝗵𝗲𝗹𝗽 🤠', callback_data='help'),
        InlineKeyboardButton('🤓 𝗮𝗯𝗼𝘂𝘁 🤓', callback_data='about')
    ], [
        InlineKeyboardButton('🔎 𝘀𝗲𝗮𝗿𝗰𝗵 🔍', switch_inline_query_current_chat='')
    ], [
        InlineKeyboardButton('👨‍💻 𝘀𝘂𝗽𝗽𝗼𝗿𝘁 👩‍💻', url='https://t.me/movie_bus6')
    ], [
        InlineKeyboardButton('🤠 𝘆𝗼𝘂 𝘁𝘂𝗯𝗲 🤠', url='https://youtube.com/channel/UCVbKgUOGVEdQlmLJ_fXrWMQ')
    ], [
        InlineKeyboardButton('🤐 𝗰𝗹𝗼𝘀𝗲 🤐', callback_data='close_data')
    ]]
@bot.on_callback_query()
async def cb_handler(bot, update):
    START_TEXT = """Hello {} 😌
            welcome to my bot 

              >> سلام خوش امدید این ربات درحال تکمیل هست .. .

              Made by @jason7108"""
    HELP_TEXT = """Hey, Follow these steps:

    Available Commands

    /start - Checking Bot Online
    /help - For more help
    /about - For more about me
    /id   -  your info on telegram 

    Made by @Jason7108 """
    ABOUT_TEXT = """--About Me-- 😎

    🤖 Name : [test bot ](https://telegram.me/{})

    👨‍💻 Developer : [Jason ](https://github.com/ir-mb/BOT1)

    📢 Channel : [bodyguard_ch](https://telegram.me/bodyguard_ch)

    🌐 Source : [👉 Click here](https://github.com/ir-mb/BOT1)

    📝 Language : [Python3](https://python.org)

Jason, [5/17/22 11:26 AM]
🧰 Framework : [Pyrogram](https://pyrogram.org)"""

    INFO_TEXT = """
    <u>💫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧</u>
     🙋🏻‍♂️ 𝐅𝐢𝐫𝐬𝐭 𝐍𝐚𝐦𝐞 : <b>{}</b>
     🧖‍♂️ 𝐒𝐞𝐜𝐨𝐧𝐝 𝐍𝐚𝐦𝐞 : <b>{}</b>
     🧑🏻‍🎓 𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞 : <b>@{}</b>
     🆔 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐃 : <code>{}</code>
     🌌 𝐏𝐫𝐨𝐟𝐢𝐥𝐞 𝐋𝐢𝐧𝐤 : <b>{}</b>
     🌍 𝐃𝐂 : <b>{}</b>
     🎤 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : <b>{}</b>
     🤠 𝐒𝐭𝐚𝐭𝐮𝐬 : <b>{}</b>
    """

    ID_TEXT = """
        🆔 𝐘𝐨𝐮𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐃 𝐢𝐬 :- <code>{}</code>
        """
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )

    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )

    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT.format((await bot.get_me()).username),
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    #
    # elif update.date == "close" :
    #     await update.message.delete()


class BaseConfig(object):
    CHNL_NAME = getenv("UPDATES_CHANNEL", "cha7108mb")
    OWNER_ID = int(getenv("OWNER_ID", 1259219363))
    LOG_CHAT =int (getenv("chat gp",1001754133791))



@bot.on_message(filters.command(
    ["start", "ping"],
    ["/", "", "?", "!", "#"]
) & filters.private)
async def start_message(client: Client, message: Message):
    dt = BaseConfig.OWNER_ID
    update_channel = BaseConfig.CHNL_NAME
    if update_channel:
        try:
            user = await bot.get_chat_member(chat_id=f'@{BaseConfig.CHNL_NAME}', user_id=message.chat.id)
            if user.status == "kicked":
               await bot.send_message(
                   chat_id=message.chat.id,
                   text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/gruprbot7108).",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Please Join My Updates Channel to use this Bot!",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Updates Channel", url=f"t.me/{BaseConfig.CHNL_NAME}")
                        ]
                    ]
                ),

            )
            return
        except Exception as e:
            await bot.send_message(
                chat_id= message.chat.id,
                text=f"Something went Wrong. Contact my [Support Group](https://t.me/Bots_Universe).\nError: {e}",
                disable_web_page_preview=True)
            return
    msg = await message.reply_text('Processing.....')
    et = await bot.get_users(dt)
    dr = et.username
    # await bot.send_animation(
    # chat_id=message.chat.id,
    # animation=BaseConfig,
    # caption=
    # await message.reply_text \
    await msg.edit_text(f'''
Hi {message.from_user.first_name}! 
            welcome to my bot 

              >> `سلام خوش امدید این ربات درحال تکمیل هست .. .`

My Owner : @{dr}
''',
                             reply_markup=START_BUTTONS)
    # return
@bot.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):

    HELP_TEXT = """**Hey, Follow these steps:

    Available Commands

    /start - Checking Bot Online
    /help - For more help
    /about - For more about me
    /id  - For  info on telegram

    Made by @jason7108 """
    await update.reply_text(
        text=HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
    )

@bot.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    ABOUT_TEXT = """--About Me-- 😎

       🤖 Name : [test bot ](https://telegram.me/{})

       👨‍💻 Developer : [Jason](https://github.com/ir-mb/BOT1)

       📢 Channel : [jason](https://telegram.me/FayasNoushad)

       🌐 Source : [👉 Click here](https://github.com/ir-mb/BOT1)

       📝 Language : [Python3](https://python.org)

       🧰 Framework : [Pyrogram](https://pyrogram.org)"""

    await update.reply_text(
        text=ABOUT_TEXT.format((await bot.get_me()).username),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )


@bot.on_callback_query()
async def cb_handler(client, query):
    if query.data == "info":
        # print(query)
        # await query.edit_message_text(query.data)
        await query.answer()
        await query.edit_message_text(
            Translation.INFO_TEXT.format(query.from_user.first_name, query.from_user.last_name,
                                         query.from_user.username, query.from_user.id, query.from_user.mention,
                                         query.from_user.dc_id, query.from_user.language_code, query.from_user.status)
        )
        return

    elif query.data == "id":
        await query.answer()
        await query.edit_message_text(
            Translation.ID_TEXT.format(query.from_user.id),reply_markup=HELP_BUTTON)


@bot.on_message((filters.command(["report"]) | filters.regex("@admins") | filters.regex("@admin"))& filters.reply& filters.group)
async def report_user(client, message):

    if message.reply_to_message:
        chat = message.chat
        your_id = message.from_user.id
        message_id = message.id
        reply = message.reply_to_message
        text = f"[Message ID:]({message.link}) `{message_id}`\n"
        text += f"[Your ID:](tg://user?id={your_id}) `{your_id}`\n"

        chat_id = message.chat.id
        reporter = str(message.from_user.id)
        mention = message.from_user.mention
        # admins = await bot.get_chat_members(chat_id=chat_id, filter="administrators")
        # success = False
        # report = f"𝖱𝖾𝗉𝗈𝗋𝗍𝖾𝗋 : {mention} ({reporter})" + "\n"
        # report += f"𝖬𝖾𝗌𝗌𝖺𝗀𝖾 : {message.reply_to_message.link}"
        info =f"""
      𝖱𝖾𝗉𝗈𝗋𝗍𝖾𝗋 : {mention} ({reporter})
      𝖬𝖾𝗌𝗌𝖺𝗀𝖾 : {message.reply_to_message.link}
"""
        reported_post = await message.reply_to_message.forward(chat_id=1259219363)
        infosend = await bot.send_message(1259219363, f"{text} ")
        getsend = await message.reply_text(f"𝖱𝖾𝗉𝗈𝗋𝗍𝖾𝖽 𝗍𝗈 𝖠𝖽𝗆𝗂𝗇𝗌! ")
    # for text in reported_post:
    # if message.reply_to_message == chat_id(1259219363):
       # await message.reply_chat_action(enums.ChatAction.)
    message = await bot.ask(owner_id,'پیام خود را ارسال کنید : ')
    print(message.text)

    await bot.send_message(chat_id ,f'\n  {text}\n user Your anser is link : {message.text}',disable_web_page_preview=True)
    # await message.reply_to_message.forward(chat_id=reporter)
    # if message.reply_to_message:
    #     reply_to_id = message.reply_to_message.message_id
    # me = await bot.get_me()
    # print(me)

    #await bot.send_message(text,f'Your anser is link : {message.text} ', disable_web_page_preview=True)
# @bot.on_message(filters.command(["id"]))
# async def id (client,message):
#     chat_id = message.chat.id
#     reporter = str(message.from_user.id)
#     reply = message.reply_to_message
#     #user = message.reply_to_message.from_user.id
#     # get = await bot.get_chat_member(message.chat.id, message.from_user.id)
#     # status = get.status
#     #mention = message.from_user.mentio
#     # else:
#     #     await message.reply_text(
#     #         "This command can only be used by the bot administrator (You're welcome)")
#
#     # async for member in bot.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
#     #     if message.reply_to_message:
#     #         get = await bot.get_chat_member(chat_id,message.from_user.id)
#     #         #if member.status == ChatMemberStatus.ADMINISTRATOR:
#     #         status = get.status
#     #         print(status)
#     #         # status = member.reply_to_message.from_user.status
#     #         user = member.status
#     #         userinfo = f"{status}".split(".")[1].capitalize()
#     if message.reply_to_message:
#         user_id = message.reply_to_message.from_user.id
#         user_name = message.reply_to_message.from_user.mention
#         #status = message.reply_to_message.from_user.status
#         await message.reply(f"User {user_name} ID is `{user_id}` \n This group's ID is `{message.chat.id}`")
#     elif (len(message.command) > 1):
#         effectiveId = message.command[1]
#         name =message.from_user.first_name
#         id = message.from_user.mention
#         if message.command[1] == message.from_user.id:
#
#             await message.reply(f"Your ID is {id}")
#     else:
#         await message.reply(f"Your ID is `{message.from_user.id}` \n This group's ID is `{message.chat.id}`")

#ho to get link group
@bot.on_message(filters.command("link"))
async def link (client, message):
    chat_id = message.chat.id
    user_id = message.from_user
    link = await bot.export_chat_invite_link(message.chat.id)
    textLINK = f"""👥 LINK Group:
    \n link🔗 :({link}))"""
    await bot.send_message(chat_id,textLINK)



@bot.on_message(filters.command(['newlink', f'set{bot.username}']))
async def newlink(client, msg):
    chat_id = msg.chat.id
    userid = msg.from_user.id
    grp_id = msg.chat.id
    admins = await bot.get_chat_member(grp_id, userid)
    if admins.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        links = await bot.create_chat_invite_link(chat_id)
        newlink = f""" new LINK Group: \n {links.date}
            \n link🔗 : {links.invite_link}"""
        await bot.send_message(chat_id,newlink)

@bot.on_message(filters.command(["time"]))
async def json (c,m):
    chat_id = m.chat.id
    time = requests.get('https://api.keybit.ir/time/')
    time = time.json()
    time2 = time["time24"]["full"]['fa']
    time1 = time["time24"]["full"]['en']# time
    day = time['date']['weekday']['name']  # day
    dayint = time['date']['day']['number']['en']
    mont = time['date']['month']['name']
    year = time['date']['year']['number']['en']
    year2 = time['date']['other']['gregorian']['iso']['en']
    dayy = f"{day} {dayint} {mont}{year}"
    tim24 = time["time12"]['shift']['full']
    await m.reply(f"""
    •تاریخ شمسی :
⏱ساعت : {time2} {tim24}
📆تاریخ امروز :{dayy}
  
•تاریخ میلادی :
⏱ساعت : {time1}
📆تاریخ امروز :{year2}
""")
   #  if m.chat.is_creator== True:
   #      await m.reply("hi")
   #  await bot.send_document(chat_id,message caption="this is a text file")
   # report_user




#
@bot.on_message(filters.command("id"))
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message
    text = f"[Message ID:]({message.link}) `{message_id}`\n"
    text += f"[Your ID:](tg://user?id={your_id}) `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await bot.get_users(split)).id
            text += f"[User ID:](tg://user?id={user_id}) `{user_id}`\n"
        except Exception:
            return await message.reply_text(message, text="This user doesn't exist.")

    text += f"[Chat ID:](https://t.me/{chat.username}) `{chat.id}`\n\n"
    if not getattr(reply, "empty", True):
        text += (
            f"[Replied Message ID:]({reply.link}) `{reply.link}`\n"
        )
        text += f"[Replied User ID:](tg://user?id={reply.from_user.id}) `{reply.from_user.id}`"

    await message.reply_text(
        text,disable_web_page_preview=True)
    # #await bot.copy_message.(message.link,BaseConfig.OWNER_ID)
    # TARGET_CHATS = -1001630620762
    #
    # #await bot.copy_message(message.chat.id,chat_id=)
    # # await client.forward_message(chat_id=190067014, from_chat_id =1259219363
    # # , message_id = update.message.message_id)
    # await bot.copy_message(chat_id=190067014, from_chat_id =1259219363)

@bot.on_message(filters.group & filters.reply & filters.command("pin"))
async def pin(client, msg):
    userid = msg.from_user.id
    grp_id = msg.chat.id
    admins = await bot.get_chat_member(grp_id, userid)
    AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())
    if admins.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await bot.pin_chat_message(grp_id, msg.reply_to_message_id)
        await msg.reply(f"is don" )
        return True
    elif admins.status  not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await msg.reply(f" not admins ")
        return False
    else:
        await bot.reply("command not filnd")




#
@bot.on_message(filters.group & filters.reply & filters.command("unpin"))
async def unpin(client, msg):
        userid = msg.from_user.id
        grp_id = msg.chat.id
        admins = await bot.get_chat_member(grp_id, userid)
        AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())
        if admins.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            #await bot.unpin_all_chat_messages(grp_id, msg.reply_to_message_id)
            await bot.unpin_chat_message(msg.chat.id)
            await msg.reply(f"is don")
            return True
        elif admins.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            await msg.reply(f" not admins ")
            return False
        else:
            await bot.reply("command not filnd")




@bot.on_message(filters.group &filters.command("bots"))
async def mu(client ,message ):
    # user_name = m.first_name
    # user_id = m.id
    # user_link = m.username
    chat_id =message.chat.id
    # await bot.send_message("me", f"NEW CHAT MEMBER {user_name}, {user_id}, {user_link}")
    # print(m)
    # bots = list(await bot.get_chat_members(
    #     chat_id,
    # #     filter=enums.ChatMembersFilter.BOTS))
    # print(bots)
    Allbots =[]
    async for member in bot.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BOTS):
        Allbots.append(member.user.mention)
    # for member in Allbots:
       # print(member)
    # async for bot in bot.get_chat_members(message.chat.id, filter=ChatMembersFilter.BOTS):
    # print(bots.user.id)
    myBot = " \n".join(f"{member} - {Allbots}" for member, Allbots in enumerate(Allbots, 1))
    # await message.reply(f" **list bots** :\n   {Allbots}\n  ")
    await message.reply(f"**List  Bots in **{message.chat.title}**  count :{len(Allbots)} \n {myBot}")

@bot.on_message(filters.command("admins"))
async def link (client, message):
    chat_id = message.chat.id
    mention = message.from_user.mention
    administrators = []
    async for member in bot.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(member.user.mention)
        #administrators.append(member.status)
        administrators.reverse()

    count = await bot.get_chat_members_count(chat_id)
    runk = member.status.value
    all = await bot.get_chat_members_count(chat_id)
    mylist = " \n".join(f"{runk}{member} - {administrators}" for member, administrators in enumerate(administrators,1))
    mylist1 = "".join(f" {member.status.OWNER}").split(".")

    #administrators.insert(member.status[1])
    await message.reply(f"**List Admins in **{message.chat.title}**  count :{len(administrators)} \n {mylist}")
    # for member in administrators:
    #     print(member.status)




    #await message.reply_text(x)




@bot.on_message(filters.command(["dump"]))
async def dumpStuff(client, message):
    if(message.from_user.id == owner_id):
        await message.reply_text(str(message.reply_to_message if message.reply_to_message else message))
    else:
        await message.reply_text(
            "This command can only be used by the bot administrator (You're welcome)")

@bot.on_message(filters.command(["setgifid", f"setgifid@{bot_username}"]))
async def setGifId(client, message):
    if(message.from_user.id == owner_id):
        try:
            animationId = message.reply_to_message.sticker.file_id
        except:
            animationId = message.command[1]
        await message.reply(animationId,animationId)
    else:
        await message.reply_text("No")
"""
Deletes the message it was replied to
Usage:
**/del**
"""
@bot.on_message(filters.command(["del", f"del@{bot_username}"]) &filters.group)
async def deleteCommand(client, message):
    chat_id =message.chat.id
    userid = message.from_user.id
    grp_id = message.chat.id
    admins = await bot.get_chat_member(grp_id, userid)
    AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())
    if admins.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if (message.from_user.id == owner_id or message.chat.get_member(message.from_user.id).can_delete_messages):
            await message.delete()
        # await bot.pin_chat_message(grp_id, message.reply_to_message_id)
            #await message.reply(f"is don")
        return True
    elif admins.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await message.reply(f" Only admins can execute this command! ")
        await message.delete()
        return False
    # if(message.chat.get_member(chat_id).can_delete_messages):
    #     if(message.from_user.id == owner_id or message.chat.get_member(message.from_user.id).can_delete_messages):
    #
    #        await message.reply_to_message.delete()
    #     else:
    #
@bot.on_message(filters.command(["eval", f"eval@{bot_username}"]))
async def evaluate(client, message, authorized=False):
    if(message.from_user.id == owner_id or authorized):
        status_message = await message.reply_text("`Running ...`")
        try:
            cmd = message.text.split(" ", maxsplit=1)[1]
        except IndexError:
            await status_message.delete()
            return
        reply_to_id = message.message_id
        if message.reply_to_message:
            reply_to_id = message.reply_to_message.message_id



@bot.on_message(filters.command(["info",'/', '!'])& filters.group)
async def info(client: Client, message: types.Message, chat: int | str = None, user: int | str = None):
    usr = await bot.get_users(message.from_user.id)
    name = usr.first_name
    bi = await bot.get_chat(message.from_user.id)
    userid = message.from_user.id
    grp_id = message.chat.id
    bio = bi.bio
    chat = message.chat.id if not chat else chat
    user = message.from_user.id if not user else user
    data = await bot.get_chat_member(chat, user)
    users = data.status.value
    # ٫rank = ['ممبر'
    # online = await bot.get_chat_online_count(chat)
    # print(online)
    from_user = None
    # from_user_id, _ = last_online(message)
    # print(from_user_id)
    if data.status.value == "member":
        rank = "کاربر عادی"
       # print(rank)
    elif (message.from_user.id == owner_id):
            rank = "سازنده ربات"
    elif data.status.value == "owner" :
        rank = "مالک گروه"
    elif data.status.value == "creator":
        rank = "سازنده گروه"
    else:
        rank ="ادمین گروه"
    #print(users)
    textinfo = (f"""
◂ نام کاربر : {message.from_user.mention} 
◂ آیدی عددی : `{message.from_user.id}`
◂ یوزرنیم : @{message.from_user.username}
◂ تعداد تصاویر پروفایل : `{message.from_user.dc_id}` عدد
◂ بیوگرافی کاربر : `{bio}` 
◂ مقام کاربر  : **{rank}**

""")
# **USER INFO**:
#     🗣 **First Name**: {message.from_user.mention}
#     🗣 **Last Name**: {message.from_user.last_name}
#     👤 **Username**: @{message.from_user.username}
#     🎖 **Rank** :**{rank}**
#     🏢 **DC ID**: `{message.from_user.dc_id}`
#     🕵️‍♂**User ID**: `{message.from_user.id}`
#     📝 **Bio**: `{bio}`
#     """)
#    # common =  await bot.get_common_chats(message.from_user.id)
#     # print(len(common))
#     # if (message.from_user.id == owner_id):
    status_message = await message.reply_text(
        "`Fetching user info...`"
    )
    await status_message.edit(
        "`Processing user info...`"
    )
    await status_message.delete()
    async for photo in bot.get_chat_photos(message.from_user.id, limit=1):
        await message.reply_photo(photo.file_id,       caption=textinfo)


@bot.on_message(filters.command(["r"]))
async def chat_member(_: Client, message: types.Message, chat: int | str = None, user: int | str = None):
    chat = message.chat.id if not chat else chat
    user = message.from_user.id if not user else user
    data = await bot.get_chat_member(chat, user)
    users = data.status.value
    print(users)

    #datastatus = (data.status).split(".")
    # a = []
    # a.append(data.status)
    # cmd = ['OWNER','ADMINISTRATOR','MEMBER','CREATOR']
    # # a = a[1]
    # for cmd  in a:
    #     if data.status ==cmd:
    #         x = cmd.value
    #         print(cmd)
@bot.on_message(filters.group & filters.command("ban")&filters.reply)
async def ban(client, message):
    userid = message.from_user.id
    grp_id = message.chat.id
    admins = await bot.get_chat_member(grp_id, userid)

    try:
        if admins.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            # await bot.delete_bot_commands(grp_id)
            # utenteban = await bot.get_users(message.text.split(" ")[1])
            utenteban = await client.get_users(message.text.split(" ")[1])
            await client.ban_chat_member(message.chat.id, utenteban.id)
            await message.reply_text(f"🚷 {message.from_user.mention} ha bannato {utenteban.mention}")

        if admins.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            await message.reply(f" Only admins can execute this command!")
    except:
        if message.reply_to_message:
            await client.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.reply_text(
                f"🚷 {message.from_user.mention} ha bannato {message.reply_to_message.from_user.mention}")
#
# #
# @bot.on_message(filters.command(["list",'/', '!'])& filters.group)
# async def info(client: Client, message: Message):
#     chat_id = message.chat.id
#     usr = await bot.get_users(message.from_user.id)
#     name = usr.first_name
#     count = await bot.get_chat_members_count(chat_id)
#     all = await bot.get_chat_members_count(chat_id)
#
#     # administrators.insert(member.status[1])

    # count = await bot.get_chat_members_count(chat_id)
    # all = await bot.get_chat_members_count(chat_id)
    # chat = await bot.get_chat(message.chat.id)

#
# @bot.on_message(filters.command(["unban", f"unban@{bot_username}"]))
# async def unban(client, message):
#     userid = message.from_user.id
#     grp_id = message.chat.id
#     admins = await bot.get_chat_member(grp_id, userid)
#     # #if(not (await bot.chat.get_member("self")).can_restrict_members):
#     #     await message.reply_text("I need additional permissions to restrict users")
#     #     return
#
#
#     try:
#         if (message.reply_to_message):
#             effectiveId = message.reply_to_message.from_user.id
#         elif (len(message.command) > 1):
#             effectiveId = message.command[1]
#         else:
#             await message.reply_text(
#                 "No user specified. Reply to the user or have their id as the argument")
#             return
#
#         if admins.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
#     #if((await bot.chat.get_member(message.from_user.id)).can_restrict_members or message.from_user.id == owner_id):
#             await bot.chat.unban_member(effectiveId)
#             await message.reply_text(
#             f"Unbanned {getFullName(await bot.get_users(effectiveId))}")
#         if admins.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
#             await message.reply(f" Only admins can execute this command!")
#     except:
#         if message.reply_to_message:
#                 await bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
#                 await message.reply_text(
#                     f"🚷 {message.from_user.mention} ha bannato {message.reply_to_message.from_user.mention}")


@bot.on_message(filters.command(["unban", "unmute"]))
async def un_ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.unban_member(
            user_id=user_id
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Okay, changed ... now "
                f"{user_first_name} To "
                " You can join the group!"
            )
        else:
            await message.reply_text(
                "Okay, changed ... now "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a> To "
                " You can join the group!"
            )
@bot.on_message(filters.command("ping"))
async def ping(_, message):
    from time import gmtime, strftime, time
    start = time()
    reply = await message.reply_text("Carico...")
    delta_ping = time() - start
    # delta_ping = time.time() - start
    # await reply.edit_text(f"**Pong!** {delta_ping * 1000:.3f} ms")
    await reply.edit_text(f"<b>Pong!</b>\n{delta_ping * 1000:.3f} ms")
    #await message.reply("Carico...",reply_markup=buttons)
# @bot.on_message(filters.command('/dc_id'))
# def f(_, m: Message):
#     if m.from_user.photo.big_file_id:
#     print(m.from_user.dc_id)

@bot.on_message(filters.command("echo"))
async def echo (client, message):
    msg = message.text.split("/echo ")
    if len(msg) == 1:
        await bot.send_message(message.chat.id, message.text)
        await bot.send_message(message.chat.id, "You entered only command.\nNext Time Try:- /echo some_text_here")
    else:
        msg = msg[1]
    await bot.send_message(message.chat.id, msg)


@bot.on_message(filters.command('deleteall'))
async def delete_all_index(bot, message):
    await message.reply_text(
        'This will delete all indexed files.\nDo you want to continue??',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                    "✓ Yes", callback_data="autofilter_delete"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Cancel ✗", callback_data="close_data"
                    )
                ],
            ]
        ),
        quote=True,
    )


@bot.on_message(filters.command(["in", "whois"]))
async def who_is(client, message):
    # https://github.com/SpEcHiDe/PyroGramBot/blob/master/pyrobot/plugins/admemes/whois.py#L19
    status_message = await message.reply_text(
        "`Fetching user info...`"
    )
    await status_message.edit(
        "`Processing user info...`"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await bot.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        return await status_message.edit("no valid user_id / message specified")
    message_out_str = ""
    message_out_str += f"<b>➨ First Name:</b> {from_user.first_name}\n"
    last_name = from_user.last_name or "<b>None</b>"
    message_out_str += f"<b>➨ Last Name:</b> {last_name}\n"
    message_out_str += f"<b>➨ Telegram ID:</b> <code>{from_user.id}</code>\n"
    username = from_user.username or "<b>None</b>"
    dc_id = from_user.dc_id or "[User Doesnt Have A Valid DP]"
    message_out_str += f"<b>➨ Data Centre:</b> <code>{dc_id}</code>\n"
    message_out_str += f"<b>➨ User Name:</b> @{username}\n"
    message_out_str += f"<b>➨ User 𝖫𝗂𝗇𝗄:</b> <a href='tg://user?id={from_user.id}'><b>Click Here</b></a>\n"
    # await message.reply_text((message_out_str))
    # file_info = get_file_id(message.reply_to_message)
    # file_info = get_file_id(message)
    # file_info = ( f"""
    # <b>{file_info.message_type}</b>:
    #         <code>{file_info.file_id}</code>\n)""")
    # await message.reply_text(file_info,
    #     quote=True
    # )
    #await from_user.photo
    # a = [x.last_online_date for x in bot.get_chat_members(message.chat.id)]
    #last = from_user.last_online_date.time("self")
#
@bot.on_message(filters.command(["json", 'js', 'showjson']))
async def jsonify(_, message):
    the_real_message = None
    reply_to_id = None

    if message.reply_to_message:
        the_real_message = message.reply_to_message
    else:
        the_real_message = message
    try:
        pk = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✗ close ✗",
                        callback_data="close_data"
                    )
                ]
            ]
        )
        await message.reply_text(f"<code>{the_real_message}</code>", reply_markup=pk, quote=True)
    except Exception as e:
        with open("json.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(the_real_message))
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✗ close ✗",
                        callback_data="close_data"
                    )
                ]
            ]
        )
        await message.reply_document(
            document="json.text",
            caption=str(e),
            disable_notification=True,
            quote=True,
            reply_markup=reply_markup
        )
        os.remove("json.text")


bot.run()
