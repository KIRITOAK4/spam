from pyrogram import Client, filters
import asyncio

API_ID = "14712540"
API_HASH = "e61b996dc037d969a4f8cf6411bb6165"
SESSION_STRING = "BQDgftwAGG8XTpVwGc4SlFQ4x6RLrNZdDI9_N5fBJMVDD7oxA-vcpGCUTkMjiz6tKyJPInWfGjrzZG4Nu1MpAQwCLkqwDAAJQ-LdYt2r9ZX6j8wUPKQ4P3bixgFA7BoZueN1yyKdLVhtUkjC-RGi-RFd4f4XEa4KycDuftJhzrXvnEwSlWjS2G8JrAD2UJB7I0JoatWvrX-atW47-BkpOUFZwID_PtT4szDcR0ki0GYb-uTI15boxsLcF8DKAAYGV_W1Jxz3uyt4Yj69XCVde4-123ytNexnaSgfjOHwY8bIJ9qCUDvFtxG9LtGJakxxMMvZ1plQLsGFeTCh8VDmUhnsgYJxIAAAAAB3wEBrAA"

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
