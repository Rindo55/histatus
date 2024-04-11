from pyrogram import Client
import requests
import time

# Initialize your Pyrogram Client
api_id = 3845818
api_hash = "95937bcf6bc0938f263fc7ad96959c6d"
bot_token = "6428443845:AAF9usGZRMRPPMuOfcjClNypt3N_p2_gUZc"

app = Client("website_status_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Function to check the website status
def check_website_status():
    url = "https://hianime.to"
    response = requests.get(url)
    if response.status_code == 200:
        return True, None
    else:
        return False, response.status_code

# Track website status changes
website_down = False

# Function to send messages to the channel
def send_message(message):
    app.send_message(-1002029401168, message)

# Main loop to check website status periodically
while True:
    website_is_down, error_code = check_website_status()
    
    if website_is_down and not website_down:
        send_message(f"**HiAnime is Reporting Error**\n\n`HTTP ERROR {error_code}`")
        website_down = True
    elif not website_is_down and website_down:
        send_message("**HiAnime is Available**\n\n`Available`")
        website_down = False
    
    # Check every 5 minutes
    time.sleep(120)

# Start the bot
app.run()
