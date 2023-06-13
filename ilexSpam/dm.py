# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝒊𝒍𝒆𝒙
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅


import asyncio

from random import choice

from pyrogram import filters, Client
from pyrogram.types import Message

from data import OneWord, RAID, THE_ILEX
from config import SUDO_USERS


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], [".", "/", "!"]))
async def dmraid(xspam: Client, message: Message):
      ilex = message.text.split(" ")

      if len(ilex) == 3:
          ok = await xspam.get_users(ilex[2])
          id = ok.id

          if id in THE_ILEX:
                await message.reply_text(f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ɪʟᴇx x`")
          elif id in SUDO_USERS:
                await message.reply_text(f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`")
          else:
              counts = int(ilex[1])
              await message.reply_text("`ᴅᴍ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.1)

      elif message.reply_to_message and (len(ilex) == 2):
          user_id = message.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id

          if id in THE_ILEX:
                await message.reply_text(f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ɪʟᴇx x`")
          elif id in SUDO_USERS:
                await message.reply_text(f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`")
          else:
              counts = int(ilex[1])
              await message.reply_text("`ᴅᴍ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.1)

      else:
            await message.reply_text("⚡ ᴜsᴀɢᴇ:\n   !dmraid 13 <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ>")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], [".", "!", "/"]))
async def dmspam(client: Client, message: Message):
    ilex = message.text.split(" ", 3)

    if  len(ilex) == 4:
        uid = int(ilex[2])
        if uid in THE_ILEX:
            await message.reply_text(f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ɪʟᴇx x`")
        elif uid in SUDO_USERS:
            await message.reply_text(f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`")
        else:
            quantity, spam_text = int(ilex[1]), ilex[3]
            await message.reply_text("`ᴅᴍ ꜱᴘᴀᴍ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
            for _ in range(quantity):
                await client.send_message(uid, spam_text)
                await asyncio.sleep(0.3)

    elif message.reply_to_message and (len(ilex) == 3):
        id = message.reply_to_message.from_user.id

        if id in THE_ILEX:
            await message.reply_text(f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ɪʟᴇx x`")
        elif id in SUDO_USERS:
            await message.reply_text(f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`")
        else:
            quantity = int(ilex[1])
            spam_text = ilex[2]
            await message.reply_text("`ᴅᴍ ꜱᴘᴀᴍ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
            for _ in range(quantity):
                await client.send_message(id, spam_text)
                await asyncio.sleep(0.3)

    else:
        await message.reply_text("😈 ᴜsᴀɢᴇ:\n .dmspam 13 <ᴜꜱᴇʀ ɪᴅ> ilex\n .dmspam 13 ilex <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>")
