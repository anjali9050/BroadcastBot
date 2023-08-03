import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6471930479:AAF9ZU9y-IoiwwIRNV91jmJfa41CLGWby40")
API_ID = int(os.environ.get("API_ID", "23560088"))
API_HASH = os.environ.get("API_HASH", "999c01704d5c417749a98f4b8785fe88")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001958949068"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5216454450").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://baba:baba@cluster0.etssakc.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
