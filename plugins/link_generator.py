#(©)Codexbotz

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "Forward the Last Message from DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://telegram.dog/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b> 𝕳𝖔𝖜 𝖙𝖔 𝖀𝖘𝖊 𝕷𝖎𝖓𝖐𝖘 ? \n 𝕾𝖙𝖊𝖕 1-  𝕮𝖑𝖎𝖈𝖐 𝖔𝖓 𝖙𝖍𝖊 𝖑𝖎𝖓𝖐 𝖆𝖓𝖉 𝖘𝖙𝖆𝖗𝖙 𝖙𝖍𝖊 𝖇𝖔𝖙 \n 𝕾𝖙𝖊𝖕 2- 𝕵𝖔𝖎𝖓 𝖙𝖍𝖊 𝖈𝖍𝖆𝖓𝖓𝖊𝖑 𝖆𝖓𝖉 𝖈𝖑𝖎𝖈𝖐 𝖔𝖓 𝖙𝖗𝖞 𝖆𝖌𝖆𝖎𝖓 𝖞𝖔𝖚  𝖜𝖎𝖑𝖑 𝖌𝖊𝖙 𝖋𝖎𝖑𝖊</b>\n\n <a href='{link}'> ░▒▓█►─═  Ŝ𝔱Ã𝐑ⓣ ═─◄█▓▒░ </a>  ", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://telegram.dog/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b> 𝕳𝖔𝖜 𝖙𝖔 𝖀𝖘𝖊 𝕷𝖎𝖓𝖐𝖘 ? \n 𝕾𝖙𝖊𝖕 1-  𝕮𝖑𝖎𝖈𝖐 𝖔𝖓 𝖙𝖍𝖊 𝖑𝖎𝖓𝖐 𝖆𝖓𝖉 𝖘𝖙𝖆𝖗𝖙 𝖙𝖍𝖊 𝖇𝖔𝖙 \n 𝕾𝖙𝖊𝖕 2- 𝕵𝖔𝖎𝖓 𝖙𝖍𝖊 𝖈𝖍𝖆𝖓𝖓𝖊𝖑 𝖆𝖓𝖉 𝖈𝖑𝖎𝖈𝖐 𝖔𝖓 𝖙𝖗𝖞 𝖆𝖌𝖆𝖎𝖓 𝖞𝖔𝖚  𝖜𝖎𝖑𝖑 𝖌𝖊𝖙 𝖋𝖎𝖑𝖊</b>\n\n <a href='{link}'> ░▒▓█►─═  Ŝ𝔱Ã𝐑ⓣ ═─◄█▓▒░ </a>  ", quote=True, reply_markup=reply_markup)
