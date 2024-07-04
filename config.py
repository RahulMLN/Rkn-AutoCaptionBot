# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Rkn_Bots(object):
    # Rkn client config
    API_ID = os.environ.get("API_ID", "25848289")
    API_HASH = os.environ.get("API_HASH", "88cf2c17c7a2bd21f4204c89c648dd40")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6725769730:AAFlMmWseDDJW3WPlGtACR3klrAs_OeAm_k")

    #start_pic
    RKN_PIC = os.environ.get("RKN_PIC", "https://telegra.ph/file/21a8e96b45cd6ac4d3da6.jpg")


    # wes response configuration
    BOT_UPTIME = time.time()
    PORT = int(os.environ.get("PORT", "8080"))
    FORCE_SUB = os.environ.get("FORCE_SUB", "-1001923834324") 
    
    # database config
    DB_NAME = os.environ.get("DB_NAME", "AutoCaption_V05_Bot")     
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://ryyadav1718:dK6yELYDYLFL2Ci2@cluster0.4cge7il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    #caption
    DEF_CAP = os.environ.get("DEF_CAP",
                             "<b><a href='telegram.me/RS_Movie'>{file_name} Telegram : @RS_Movie\n\nForward the file before Downloading.</a></b>",
    )

    #sticker Id
    STICKER_ID = os.environ.get("STICKER_ID", "CAACAgIAAxkBAAELFqBllhB70i13m-woXeIWDXU6BD2j7wAC9gcAAkb7rAR7xdjVOS5ziTQE")

    #admin id
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1557042262').split()]
    

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
