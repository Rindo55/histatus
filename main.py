from pyrogram import Client, filters
import requests
import time
import asyncio
# Initialize the Pyrogram Client
api_id = 3845818
api_hash = "95937bcf6bc0938f263fc7ad96959c6d"
bot_token = "6428443845:AAF9usGZRMRPPMuOfcjClNypt3N_p2_gUZc"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Website URL to check
url = "https://hianime.to"
website_down = False

# Function to check the website status
def check_website_status():
    global website_down
    try:
        response = requests.get(url)
        if response.status_code != 200:
            if not website_down:
                app.send_message(-1002029401168, f"HiAnime is Reporting Error\nHTTP ERROR {response.status_code}")
                website_down = True
        else:
            if website_down:
                app.send_message(-1002029401168, "HiAnime is Available\nAvailable")
                website_down = False
    except requests.ConnectionError:
        if not website_down:
            app.send_message(-1002029401168, "HiAnime is Reporting Error\nConnection Error")
            website_down = True

# Background task to check website status every minute
async def check_website():
    while True:
        check_website_status()
        time.sleep(60)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text("Bot Started!")

# Start te bot and the background task
async def main():
    task = asyncio.create_task(check_website())
    await app.start()
    await task

asyncio.run(main())
