from environs import Env


env = Env()
env.read_env()

# BOT_TOKEN = env.str("BOT_TOKEN")  
# ADMINS = env.list("ADMINS")  
# IP = env.str("ip")  

# DB_USER = env.str("DB_USER")
# DB_PASS = env.str("DB_PASS")
# DB_NAME = env.str("DB_NAME")
# DB_HOST = env.str("DB_HOST")

import os

BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
ADMINS = list(os.environ.get("ADMINS"))
IP = str(os.environ.get("ip"))
PROVIDER_TOKEN = str(os.environ.get("PROVIDER_TOKEN"))
