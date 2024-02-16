from pyrogram import Client, filters
from pyrogram.types import Message
import time

API_ID = "your_api_id"
API_HASH = "your_api_hash"

app = Client("user_session", api_id=API_ID, api_hash=API_HASH)

# Dictionary to store chat ID for each user
user_chat_ids = {}

@app.on_message(filters.command("delay", prefixes="/"))
def delay_command_handler(client: Client, message: Message):
    if message.from_user and message.from_user.is_member:
        try:
            command_parts = message.text.split(" ")
            if len(command_parts) >= 4:
                _, _, text_to_send, seconds_str, times_str = command_parts
                seconds = int(seconds_str)
                times = int(times_str)

                # Store chat ID for the user
                user_chat_ids[message.from_user.id] = message.chat.id

                for _ in range(times):
                    time.sleep(seconds)
                    # Use stored chat ID to reply
                    client.send_message(user_chat_ids[message.from_user.id], text_to_send)

            else:
                message.reply_text("Invalid command format. Use /delay <text_to_send> <seconds> <times>")
        except Exception as e:
            print(f"Error: {str(e)}")
            message.reply_text("An error occurred while processing the command.")
    else:
        message.reply_text("You need to be a member of the chat to use this command.")

app.run()
