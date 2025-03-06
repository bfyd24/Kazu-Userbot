from telethon import Button
from AyiinXd import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    STRING_SESSION,
    blacklistayiin,
    bot,
    tgbot,
)

async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/78fbd9d73e1f456857222.jpg",
                caption="𝗠𝗼𝗻𝘁𝗼𝗺𝗸-Userbot.\n     **status : Active\n     ketik `.ping` untuk cek bot!**",
                buttons=[(Button.url("Channel", "https://t.me/montomk")),
                         (Button.url("Support", "https://t.me/zorthsupport"))]
            )
    except Exception as e:
        LOGS.error(e)
        return None
