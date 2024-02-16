from pyrogram import Client, filters
from pyrogram.types import Message
import time

# List of dictionaries containing API credentials
api_credentials_list = [
    {"api_id": "14712540" , "api_hash": "e61b996dc037d969a4f8cf6411bb6165"},
    {"api_id": "15356238", "api_hash": "9af2a934037de907d317abc8ad049c36"},
    # Add more sets of API credentials as needed
]

# Dictionary to store chat ID for each user
user_chat_ids = {}

# Function to handle the /delay command
def delay_command_handler(client: Client, message: Message, api_credentials):
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
                    # Use stored chat ID and current API credentials to reply
                    with Client(f"user_session_{api_credentials['api_id']}", **api_credentials) as temp_client:
                        temp_client.send_message(user_chat_ids[message.from_user.id], text_to_send)

            else:
                message.reply_text("Invalid command format. Use /delay <text_to_send> <seconds> <times>")
        except Exception as e:
            print(f"Error: {str(e)}")
            message.reply_text("An error occurred while processing the command.")
    else:
        message.reply_text("You need to be a member of the chat to use this command.")

# Iterate over each set of API credentials and run the client
for api_credentials in api_credentials_list:
    app = Client(f"user_session_{api_credentials['api_id']}", **api_credentials)
    app.add_message_handler(delay_command_handler, filters.command("delay", prefixes="/"))
    app.run()
