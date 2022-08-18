from pyrogram import *
from pyrogram.types import *
from pyrogram.owl import *
from config import *
import random

Owl = Client(
     "Dark_Owl",
     api_id=API_ID,
     api_hash=API_HASH,
     bot_token=BOT_TOKEN
)


@Owl.on_message(filters.private & filters.command("start")) 
async def start(bot, message):
    mr = await bot.get_me()   
    await message.reply_photo(
        photo=random.choice(PHOTO),
        caption=START_TEXT.format(user=message.from_user.mention, bot=mr.mention),
        reply_markup=InlineKeyboardMarkup(ST_BUTTON),
        parse_mode=enums.ParseMode.HTML                              
    ) 

@Owl.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    mr = await client.get_me()   
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=START_TEXT.format(user=query.from_user.mention, bot=mr.mention),
            reply_markup=InlineKeyboardMarkup(ST_BUTTON),
            parse_mode=enums.ParseMode.HTML
        )

    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(mr.mention, __version__),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(ABT_BUTTON),
            parse_mode=enums.ParseMode.HTML
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()

       

@Owl.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    chat_id = message.from_user.id
    if message.from_user.id == ADMIN:
        await reply_text(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    await bot.send_message(
        chat_id=ADMIN,
        text=TEXT.format(id=info.id, name=info.mention, un=info.username, msg=message.text),
        parse_mode=enums.ParseMode.HTML
    ) 

@Owl.on_message(filters.private & filters.media)
async def pm_media(bot, message):
    chat_id = message.from_user.id

    if message.from_user.id == ADMIN:
        await replay_media(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)   
    await bot.copy_message(
        chat_id=ADMIN,
        from_chat_id=message.chat.id,
        message_id=message.id,
        caption=MEDIA.format(id=info.id, name=info.mention, un=info.username),
        parse_mode=enums.ParseMode.HTML
    )


@Owl.on_message(filters.user(ADMIN) & filters.text)
async def reply_text(bot, message):
    chat_id = message.from_user.id
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.send_message(
            chat_id=int(reference_id),
            text=message.text
        )

@Owl.on_message(filters.user(ADMIN) & filters.media)
async def replay_media(bot, message):
    chat_id = message.from_user.id
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.copy_message(
            chat_id=int(reference_id),
            from_chat_id=message.chat.id,
            message_id=message.id,
            parse_mode=enums.ParseMode.HTML
        )


print("🚀 Bot is starting.........🔥")
Owl.run()


