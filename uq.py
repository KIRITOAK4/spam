from pyrogram import Client, filters
import asyncio

API_ID = "14712540"
API_HASH = "e61b996dc037d969a4f8cf6411bb6165"

app = Client("user_session", api_id=API_ID, api_hash=API_HASH)

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
