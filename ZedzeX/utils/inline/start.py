from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✯ 𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 ✯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝗛𝗲𝗹𝗽 ✯",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="✯ 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀 ✯", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✯ 𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 ✯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝗢𝘄𝗻𝗲𝗿 ✯", url=f"https://t.me/VIP_Boy_113"
            ),
            InlineKeyboardButton(
                text="✯ 𝗛𝗲𝗹𝗽 ✯", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 ✯", url=f"https://t.me/vip_world_op",
            ),
            InlineKeyboardButton(
                text="✯ 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 ✯", url=f"https://t.me/RED_DRAGON_CLAN",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝗦𝗼𝘂𝗿𝗲𝗰 ✯",
                url=f"https://github.com/RohitXBot/RohitXMusic",
            )
        ],
     ]
    return buttons
