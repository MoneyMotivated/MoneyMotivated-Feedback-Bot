import os

ADMIN = int(os.environ.get('ADMIN', ''))

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

PHOTO = os.environ.get("PHOTO", "https://telegra.ph/file/cbee88c58fd6708ddfe90.jpg https://telegra.ph/file/9fffc01c8477044d9c14e.jpg").split()

START_TEXT = os.environ.get("START_TEXT", "Hai {user}  👋\n\nI am {bot} official assistant bot. please contact my owners with use me 🤩 please send any message") 

##=================[ ALL TEXT'S ]===============##

TEXT = """Message From: <code>{id}</code>
Name: {name}
UN: @{un}

{msg}"""

MEDIA = """Message From: <code>{id}</code>
Name: {name}
UN: @{un}"""


