import os

ADMIN = int(os.environ.get('ADMIN', '5418882619'))

API_ID = int(os.environ.get("API_ID", "11344399"))

API_HASH = os.environ.get("API_HASH", "36VMz3kzFSnFHkfgTXr7Wdx9bx5HCF8tSs")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5718362115:AAH7lm6iNkaZivnmHs3KKb_gwsvPTVo09FQ")

PHOTO = os.environ.get("PHOTO", "https://telegra.ph/file/cbee88c58fd6708ddfe90.jpg https://telegra.ph/file/9fffc01c8477044d9c14e.jpg").split()

START_TEXT = os.environ.get("START_TEXT", "Hai {user}  👋\n\nI am {bot} official assistant bot. please contact my owners with use me 🤩 please send any message") 

##=================[ ALL TEXT'S ]===============##

TEXT = """ID: <code>{id}</code>
Name: {name}
UN: @{un}

{msg}"""

MEDIA = """ID: <code>{id}</code>
Name: {name}
UN: @{un}"""


