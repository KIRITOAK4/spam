from pyrogram import Client, filters
from pyrogram.types import Message
import time, schedule

# List of dictionaries containing API credentials
api_credentials_list = [
    {"api_id": "14712540" , "api_hash": "e61b996dc037d969a4f8cf6411bb6165"},
    {"api_id": "15356238", "api_hash": "9af2a934037de907d317abc8ad049c36"},
    # Add more sets of API credentials as needed
]

user_messages = {}

def create_client(api_credentials):
    app = Client(f"user_session_{api_credentials['api_id']}", **api_credentials)

    @app.on_message(filters.command("delay", prefixes="/"))
    def delay_command_handler(client: Client, message: Message):
        try:
            command_parts = message.text.split(" ")
            if len(command_parts) >= 4:
                _, command_to_send, seconds_str, times_str = command_parts
                seconds = int(seconds_str)
                times = int(times_str)

                # Store chat ID and text message for the user
                user_messages[message.chat.id] = {"text": text_to_send, "times": times}

                message.reply_text(f"Delayed message stored. It will be sent {times} times after {seconds} seconds.")
            else:
                message.reply_text("Invalid command format. Use /delay <text_to_send> <seconds> <times>")
        except Exception as e:
            print(f"Error: {str(e)}")
            message.reply_text("An error occurred while processing the command.")

    return app

# Function to send the delayed messages
def send_delayed_messages():
    for chat_id, data in user_messages.items():
        text_to_send = data["text"]
        times = data["times"]
        for _ in range(times):
            app.send_message(chat_id, text_to_send)

# Iterate over each set of API credentials and run the client
for api_credentials in api_credentials_list:
    app = create_client(api_credentials)
    app.run()

# Schedule the delayed message sender to run every minute
schedule.every(1).minutes.do(send_delayed_messages)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
