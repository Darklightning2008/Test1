from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto

# Replace "YOUR_API_ID" and "YOUR_API_HASH" with your own values
api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"

app = Client("my_bot", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.command("start"))
def start(client, message):
    user = message.from_user.first_name
    caption1 = f"Hello {user}"
    caption2 = ("I Aᴍ Yᴏᴜʀ TRUNKS. DRAGON BALL ᴛʜᴇᴍᴇᴅ ᴍᴀɴɢᴇᴍᴇɴᴛ ʙᴏᴛ ᴀɴᴅ ᴍᴜsɪᴄ ʙᴏᴛ\n"
                "▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n"
                "🌌 Cᴏɴᴛʀᴏʟ Yᴏᴜʀ Gʀᴏᴜᴘ Eғғᴏʀᴛʟᴇssʟʏ.Tʏᴘᴇ /help Tᴏ Uɴᴠᴇɪʟ Yᴏᴜʀ Lᴏᴠᴇ.\n"
                "Lᴇᴛ's Bʀɪɴɢ Oʀᴅᴇʀ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ!")
    
    # Send the first image with caption
    client.send_photo(message.chat.id, photo="https://example.com/image1.jpg", caption=caption1)
    
    # Send the second image with caption
    client.send_photo(message.chat.id, photo="https://example.com/image2.jpg", caption=caption2)

app.run()
