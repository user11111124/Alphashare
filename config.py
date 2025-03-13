from typing import List, Dict
import os
from dotenv import load_dotenv


load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv("7971581858:AAHGWOH_W8f9PnZ2U8BgJrjxhDdfaCwMW0E")
API_ID = int(os.getenv("27810925"))
API_HASH = os.getenv("04b5c9dd67d1e551ac2f62f25b2d1aad")

# Database Configuration
MONGO_URI = os.getenv("mongodb+srv://XTV:CLLEls0jF9DbITqi@cluster0.10z7p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.getenv("Cluster0")

# Channel Configuration
DB_CHANNEL_ID = int(os.getenv("-1002569527014"))
FORCE_SUB_CHANNEL = int(os.getenv("-1002243932904"))

# Bot Information
BOT_USERNAME = os.getenv("xtvfile2bot")
BOT_NAME = os.getenv("𝕏-FileStore 2.1")
BOT_VERSION = "1.0"

# Links
CHANNEL_LINK = os.getenv("t.me/xtveurope")
DEVELOPER_LINK = os.getenv("t.me/davdxp")
SUPPORT_LINK = os.getenv("t.me/xtveurope")

# Admin IDs - Convert space-separated string to list of integers
ADMIN_IDS: List[int] = [
    int(admin_id.strip())
    for admin_id in os.getenv("ADMIN_IDS", "6820461647").split()
    if admin_id.strip().isdigit()
]

# File size limit (2GB in bytes)
MAX_FILE_SIZE = 2000 * 1024 * 1024

# Supported file types and extensions
SUPPORTED_TYPES = [
    "document",
    "video",
    "audio",
    "photo",
    "voice",
    "video_note",
    "animation"
]

SUPPORTED_EXTENSIONS = [
    # Documents
    "pdf", "txt", "doc", "docx", "xls", "xlsx", "ppt", "pptx",
    # Programming Files
    "py", "js", "html", "css", "json", "xml", "yaml", "yml",
    # Archives
    "zip", "rar", "7z", "tar", "gz", "bz2",
    # Media Files
    "mp4", "mp3", "m4a", "wav", "avi", "mkv", "flv", "mov",
    "webm", "3gp", "m4v", "ogg", "opus",
    # Images
    "jpg", "jpeg", "png", "gif", "webp", "bmp", "ico",
    # Applications
    "apk", "exe", "msi", "deb", "rpm",
    # Other
    "txt", "text", "log", "csv", "md", "srt", "sub"
]

SUPPORTED_MIME_TYPES = [
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/zip",
    "application/x-rar-compressed",
    "application/x-7z-compressed",
    "video/mp4",
    "audio/mpeg",
    "audio/mp4",
    "image/jpeg",
    "image/png",
    "image/gif",
    "application/vnd.android.package-archive",
    "application/x-executable",
]

class Messages:
    START_TEXT = """
🎉 **Welcome to {bot_name}!** 🎉

Hello {user_mention}! I'm your secure file sharing assistant.

🔐 **Key Features:**
• Secure File Sharing
• Unique Download Links
• Multiple File Types Support
• Real-time Tracking
• Force Subscribe

📢 Join @XTVeurope for updates!
👨‍💻 Contact @davdxp for support

Use /help to see available commands!
"""

    HELP_TEXT = """
📚 **Available Commands** 

👤 **User Commands:**
• /start - Start bot
• /help - Show this help
• /about - About bot

👑 **Admin Commands:**
• /upload - Upload file (reply to file)
• /stats - View statistics
• /broadcast - Send broadcast
• Auto-Delete Feature:
Files are automatically deleted after the set time.
Use /auto_del to change the deletion time.

📝 **Supported File Types:**
• Documents (PDF, DOC, XLS, etc.)
• Videos (MP4, MKV, AVI, etc.)
• Audio (MP3, M4A, WAV, etc.)
• Images (JPG, PNG, GIF, etc.)
• Archives (ZIP, RAR, 7Z, etc.)
• Applications (APK, EXE, etc.)
• Other Formats

⚠️ For support: @davdxp
"""

    ABOUT_TEXT = """
ℹ️ **About {bot_name}**

**Version:** `{version}`
**Developer:** @davdxp
**Language:** Python
**Framework:** Pyrogram

📢 **Updates:** @XTVeurope
🛠 **Support:** @XTV_official

**Features:**
• Secure File Sharing
• Force Subscribe
• Admin Controls
• Real-time Stats
• Multiple File Types
• Enhanced Security
• Automatic File Type Detection

Made with ❤️ by @davdxp
"""

    FILE_TEXT = """
📁 **File Details**

**Name:** `{file_name}`
**Size:** {file_size}
**Type:** {file_type}
**Downloads:** {downloads}
**Uploaded:** {upload_time}

🔗 **Share Link:**
`{share_link}`
"""

    FORCE_SUB_TEXT = """
⚠️ **Access Restricted!**

Please join our channel to use this bot:

Click button below, then try again!
"""

class Buttons:
    def start_buttons() -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Help 📚", "callback_data": "help"},
                {"text": "About ℹ️", "callback_data": "about"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK},
                {"text": "Developer 👨‍💻", "url": DEVELOPER_LINK}
            ]
        ]

    def help_buttons() -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Home 🏠", "callback_data": "home"},
                {"text": "About ℹ️", "callback_data": "about"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK}
            ]
        ]

    def about_buttons() -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Home 🏠", "callback_data": "home"},
                {"text": "Help 📚", "callback_data": "help"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK}
            ]
        ]

    def file_buttons(file_uuid: str) -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Download 📥", "callback_data": f"download_{file_uuid}"},
                {"text": "Share 🔗", "callback_data": f"share_{file_uuid}"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK}
            ]
        ]


class Progress:
    PROGRESS_BAR = "█"
    EMPTY_PROGRESS_BAR = "░"
    PROGRESS_TEXT = """
**{0}** {1}% 

**⚡️ Speed:** {2}/s
**💫 Done:** {3}
**💭 Total:** {4}
**⏰ Time Left:** {5}
"""
