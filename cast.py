from os import environ

from pyrogram.client import bot
import admin_check
import re
from pyrogram import filters
id_pattern = re.compile(r'^.\d+$')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
def f_sudo_filter(filt, client, message):
    return bool(
        message.from_user.id in ADMINS
    )


sudo_filter = filters.create(
    func=f_sudo_filter,
    name="SudoFilter"
)


def onw_filter(filt, client, message):
    if ADMINS:
        return bool(
            True # message.from_user.id in ADMINS
        )
    else:
        return bool(
            message.from_user and
            message.from_user.is_self
        )


f_onw_fliter = filters.create(
    func=onw_filter,
    name="OnwFilter"
)


async def admin_filter_f(filt, client, message):
    return await admin_check(message)


admin_fliter = filters.create(
    func=admin_filter_f,
    name="AdminFilter"
)