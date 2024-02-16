from pyrogram import Client, filters
import asyncio
from config import API_ID, API_HASH, SESSION_STRING
#API_ID = 14712540
#API_HASH = "e61b996dc037d969a4f8cf6411bb6165"
#SESSION_STRING = "BQDgftwAwtNx7rFmWHT9jIpbD-N-j95sBQTQl63jSIW7x_ihPU-kxXwv1frmljeRZbyOFq0dmcCSe9Cq7fOFqVMA61JZnh0TOOZcqlLOdFNkMNPAYisMcoWYD6PVqJy6rqPsOqHd9ff3ib60WCcdJoPeKWLNJJMgox_4YXtVBwW6dt8bKbfemMKcns6BADkInojvvQGFGm9nCbf3S15nklH8dmmNllene6T-x4j8BQW_5puTv38M0cM5jIbclsdRTKuQAaofdieCjgLmFCK7JJawrihxvzViZRDO-TlEkftUw8T4Hzce7eQfRBJN3PcOtHAJY4XwbbuFFq_fCw_pcwZBkC2lHAAAAAB3wEBrAA"

app = Client("user_session", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

@app.on_message(filters.command("delayspam", prefixes="/"))
async def delayspam_command_handler(client, message):
    try:
        command_parts = message.text.split(" ", 3)
        delay = float(command_parts[1])
        count = int(command_parts[2])
        msg = str(command_parts[3])
    except (IndexError, ValueError):
        return await message.reply_text(f"**Usage :** /delayspam <delay time> <count> <msg>")

    try:
        for i in range(count):
            await message.reply_text(msg)
            await asyncio.sleep(delay)
    except Exception as u:
        await message.reply_text(f"**Error :** `{u}`")

app.run()
