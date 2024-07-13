import asyncio
import importlib
from pyrogram import idle
from rankbot import rankbot
from rankbot.modules import ALL_MODULES

LOGGER_ID = -1001919135283

loop = asyncio.get_event_loop()

async def daxxpapa_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("rankbot.modules." + all_module)
    print("𝖻𝗈𝗍 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝗌𝗍𝖺𝗋𝗍")
    await idle()
    print("𝖯𝗂𝗋𝗈 𝖢𝗈𝖽𝖾𝗋 akira made me")
    await rankbot.send_message(LOGGER_ID, "**𝖨 𝖺𝗆 𝖺𝗅𝗂𝗏𝖾 𝖡𝖺𝖻𝗒 𝖸𝗈𝗎𝗋 𝖡𝗈𝗍 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝖣𝖾𝗉𝗅𝗈𝗒 \n Mʏ Dᴇᴠᴇʟᴏᴘᴇʀ  [AKIRA](https://t.me/AKIRA_ISHIKKI)**")

if __name__ == "__main__":
    loop.run_until_complete(daxxpapa_boot())
    
