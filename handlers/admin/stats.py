from pyrogram import Client, filters
from pyrogram.types import Message
from database import Database
from utils import is_admin, humanbytes
import config

db = Database()

@Client.on_message(filters.command("stats"))
async def stats_command(client: Client, message: Message):
    if not is_admin(message):
        await message.reply_text("⚠️ You are not authorized to view stats!")
        return
    
    stats = await db.get_stats()
    stats_text = (
        "📊 **Bot Statistics**\n\n"
        f"📁 Files: {stats['total_files']}\n"
        f"👥 Users: {stats['total_users']}\n"
        f"📥 Downloads: {stats['total_downloads']}\n"
        f"💾 Size: {humanbytes(stats['total_size'])}\n"
        f"🕒 Auto-Delete Files: {stats.get('active_autodelete_files', 0)}\n\n"
        f"⏱ Current Auto-Delete Time: {getattr(config, 'DEFAULT_AUTO_DELETE', 15)} minutes"
    )
    await message.reply_text(stats_text)
