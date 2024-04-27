from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto

# Replace "YOUR_API_ID" and "YOUR_API_HASH" with your own values
api_id = "22839370"
api_hash = "7fb99db07ddecec3e7a1f02da9730c33"

app = Client("6799162039:AAFt_KeEtS6w3WNUOCnvyjYU9elUDKsHTgY", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.command("start"))
def start(client, message):
    user = message.from_user.first_name
    caption1 = f"Hello {user}"
    caption2 = ("I Aᴍ Yᴏᴜʀ TRUNKS. DRAGON BALL ᴛʜᴇᴍᴇᴅ ᴍᴀɴɢᴇᴍᴇɴᴛ ʙᴏᴛ ᴀɴᴅ ᴍᴜsɪᴄ ʙᴏᴛ\n"
                "▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n"
                "🌌 Cᴏɴᴛʀᴏʟ Yᴏᴜʀ Gʀᴏᴜᴘ Eғғᴏʀᴛʟᴇssʟʏ.Tʏᴘᴇ /help Tᴏ Uɴᴠᴇɪʟ Yᴏᴜʀ Lᴏᴠᴇ.\n"
                "Lᴇᴛ's Bʀɪɴɢ Oʀᴅᴇʀ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ!")
    
    # Send the first image with caption
    client.send_photo(message.chat.id, photo="https://graph.org/file/3d03ef874b730efa709b7.jpg", caption=caption1)
    
    # Send the second image with caption
    client.send_photo(message.chat.id, photo="https://graph.org/file/41ac1b364652b975fbb50.jpg", caption=caption2)

app.run()
