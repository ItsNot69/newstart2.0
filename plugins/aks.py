import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatJoinRequest
from info import CHAT_ID, APPROVED 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def aksapprove(client, message: ChatJoinRequest):
    chat=message.chat 
    user=message.from_user 
    print(f"{user.first_name} Joined") 
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "True":
        buttons = [[
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ​', url=f'https://t.me/born4movies7')
            
        ]]
        markup = InlineKeyboardMarkup(buttons)
        caption = f"<b>Dᴇᴀʀ {message.from_user.mention()},\n\nYour Request To Jᴏɪɴ {message.chat.title} Was Approved ✅</b>"
        await client.send_photo(
            message.from_user.id, 
            photo='https://telegra.ph/file/1ad6bc399ca2002969ccf.jpg', 
            caption=caption, 
            reply_markup=markup
        )












