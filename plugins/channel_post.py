#(©)Codexbotz

import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from helper_func import encode

@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.command(['start','users','broadcast','batch','genlink','stats']))
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("Please Wait...!", quote = True)
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return
    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://telegram.dog/{client.username}?start={base64_string}"

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])

    await reply_text.edit(f"<b> 𝕳𝖔𝖜 𝖙𝖔 𝖀𝖘𝖊 𝕷𝖎𝖓𝖐𝖘 ? \n 𝕾𝖙𝖊𝖕 1-  𝕮𝖑𝖎𝖈𝖐 𝖔𝖓 𝖙𝖍𝖊 𝖑𝖎𝖓𝖐 𝖆𝖓𝖉 𝖘𝖙𝖆𝖗𝖙 𝖙𝖍𝖊 𝖇𝖔𝖙 \n 𝕾𝖙𝖊𝖕 2- 𝕵𝖔𝖎𝖓 𝖙𝖍𝖊 𝖈𝖍𝖆𝖓𝖓𝖊𝖑 𝖆𝖓𝖉 𝖈𝖑𝖎𝖈𝖐 𝖔𝖓 𝖙𝖗𝖞 𝖆𝖌𝖆𝖎𝖓 𝖞𝖔𝖚  𝖜𝖎𝖑𝖑 𝖌𝖊𝖙 𝖋𝖎𝖑𝖊</b>\n\n <a href='{link}'> ░▒▓█►─═  Ŝ𝔱Ã𝐑ⓣ ═─◄█▓▒░ </a>  ", reply_markup=reply_markup, disable_web_page_preview = True)

    if not DISABLE_CHANNEL_BUTTON:
        await post_message.edit_reply_markup(reply_markup)

@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://telegram.dog/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass
