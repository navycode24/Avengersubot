import os
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool
TIME_LIMIT = int(getenv("TIME_LIMIT", "2592000"))
TIME_SLEEP = int(getenv("TIME_SLEEP", "86400"))

load_dotenv(".env")


API_ID = int(getenv("API_ID", "")) #optional
API_HASH = getenv("API_HASH", "")
MONGO_URL = getenv("MONGO_URL")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
DEEP_AI = getenv("DEEP_AI", "d7394561-0528-4714-a1ee-edd7020b48e1")
OWNER_ID = int(getenv("OWNER_ID") or 0)
ADMIN1_ID = list(map(int, getenv("ADMIN1_ID", "1054295664").split()))
ADMIN2_ID = list(map(int, getenv("ADMIN2_ID", "1755047203").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://naya:eF15I6lX34892tOG@nayapremium-78e01d94.mongo.ondigitalocean.com/admin?authSource=admin&replicaSet=nayapremium&tls=true")

ADMIN1_ID.append(1054295664)
ADMIN2_ID.append(1755047203)


BOT_TOKEN = getenv("BOT_TOKEN")
BOT_WORKERS = int(getenv("BOT_WORKERS", "2"))
USER_WORKERS = int(getenv("BOT_WORKERS", "8"))
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", None)
OPENAI_API = getenv("OPENAI_API", "")
DB_URL = getenv("DATABASE_URL", "postgresql://doadmin:AVNS_5AiLC4zTp4uyiNDjUBD@dbaas-db-1730433-do-user-13904317-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_WORKERS = int(getenv("BOT_WORKERS", "2"))
USER_WORKERS = int(getenv("BOT_WORKERS", "8"))
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "azazel") #don't change
REPO_URL = getenv("REPO_URL", "https://github.com/ayrizz/Azazel-Project")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SUPPORT = int(getenv("SUPPORT", "-1001812143750"))
CHANNEL = int(getenv("CHANNEL", "-1001896537650"))


COMMM_AND_PRE_FIX = getenv("COMMM_AND_PRE_FIX", "/")
START_COMMAND = getenv("START_COMMAND", "deploy")
SESI_COMMAND = getenv("SESI_COMMAND", "tampil")
SESIID_COMMAND = getenv("SESI_COMMAND", "cari")
LOG_FILE_ZZGEVC = getenv("LOG_FILE_ZZGEVC", "Ubot.log")

AKTIFSESI = {}
# /start message when other users start your bot
SESI_OTHER_USERS_TEXT = getenv(
    "SESI_OTHER_USERS_TEXT",
    (
        """
        TAMPIL SESI : 
        """
    )
)
AKTIFSESIID = {}
# /start message when other users start your bot
SESIID_OTHER_USERS_TEXT = getenv(
    "SESI_OTHER_USERS_TEXT",
    (
        """
        Fitur ini untuk cari sesi string yang sudah menggunakan bot ini
        """
    )
)
AKTIFPERINTAH = {}
START_OTHER_USERS_TEXT = getenv(
    "START_OTHER_USERS_TEXT",
    (
        f"""
        👋 **Halo Saya Adalah New-Ubot Pyro**
        """
    )
)
INPUT_PHONE_NUMBER = getenv("INPUT_PHONE_NUMBER", (
    "Masukan nomor akun telegram anda dengan diawali +, Contoh +62xxxx"
))
RECVD_PHONE_NUMBER_DBP = getenv("RECVD_PHONE_NUMBER_DBP", (
    "Mohon periksa pesan masuk anda, dan masukkan kode yang ada dengan menggunakan spasi setiap kode\n Contoh : 1 2 3 4 5"
))
ALREADY_REGISTERED_PHONE = getenv("ALREADY_REGISTERED_PHONE", (
    "Mencoba mengirikan kode OTP"
))
CONFIRM_SENT_VIA = getenv("CONFIRM_SENT_VIA", (
    "Mohon periksa pesan masuk anda, dan masukkan semua kode 𝗱𝗶𝗺𝗮𝗻𝗮 𝗼𝘁𝗽 𝗮𝗻𝗴𝗸𝗮 𝗱𝗶𝗱𝗮𝗵𝘂𝗹𝘂𝗸𝗮𝗻 𝗱𝗮𝗻 𝗱𝗶𝗯𝗲𝗿𝗶 𝘀𝗽𝗮𝘀𝗶 𝗱𝗶𝘁𝗮𝗺𝗯𝗮𝗵 𝘀𝗲𝗹𝘂𝗿𝘂𝗵 𝗸𝗼𝗱𝗲 𝘀𝘁𝗿𝗶𝗻𝗴 𝘁𝗮𝗻𝗽𝗮 𝘀𝗽𝗮𝘀𝗶\n Contoh : 3 0 0 5 7"
))
RECVD_PHONE_CODE = getenv("RECVD_PHONE_CODE", (
    "Mencoba mengirikan kode OTP"
))
NOT_REGISTERED_PHONE = getenv("NOT_REGISTERED_PHONE", (
    "Maaf Nomor Yang Anda Masukkan Belum Terdaftar"
))
PHONE_CODE_IN_VALID_ERR_TEXT = getenv(
    "Kode yang anda masukkan salah, coba masukin kembali atau mulai dari awal"
)
TFA_CODE_IN_VALID_ERR_TEXT = getenv(
    "Kode yang anda masukkan salah, coba masukin kembali atau mulai dari awal"
)
ACC_PROK_WITH_TFA = getenv("ACC_PROK_WITH_TFA", (
    "Verifikasi 2 Langkah Diaktifkan, Mohon Masukkan Verifikasi 2 Langkah Anda."
))
SESSION_GENERATED_USING = getenv("SESSION_GENERATED_USING", (
    "Ubot sudah aktif, Hubungi Admins Untuk MeRestart Bot ..."
))

SESSION1 = getenv("SESSION1", "")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
SESSION11 = getenv("SESSION11", "")
SESSION12 = getenv("SESSION12", "")
SESSION13 = getenv("SESSION13", "")
SESSION14 = getenv("SESSION14", "")
SESSION15 = getenv("SESSION15", "")
SESSION16 = getenv("SESSION16", "")
SESSION17 = getenv("SESSION17", "")
SESSION18 = getenv("SESSION18", "")
SESSION19 = getenv("SESSION19", "")
SESSION20 = getenv("SESSION20", "")
SESSION21 = getenv("SESSION21", "")
SESSION22 = getenv("SESSION22", "")
SESSION23 = getenv("SESSION23", "")
SESSION24 = getenv("SESSION24", "")
SESSION25 = getenv("SESSION25", "")
SESSION26 = getenv("SESSION26", "")
SESSION27 = getenv("SESSION27", "")
SESSION28 = getenv("SESSION28", "")
SESSION29 = getenv("SESSION29", "")
SESSION30 = getenv("SESSION30", "")
SESSION31 = getenv("SESSION31", "")
SESSION32 = getenv("SESSION32", "")
SESSION33 = getenv("SESSION33", "")
SESSION34 = getenv("SESSION34", "")
SESSION35 = getenv("SESSION35", "")
SESSION36 = getenv("SESSION36", "")
SESSION37 = getenv("SESSION37", "")
SESSION38 = getenv("SESSION38", "")
SESSION39 = getenv("SESSION39", "")
SESSION40 = getenv("SESSION40", "")
SESSION41 = getenv("SESSION41", "")
SESSION42 = getenv("SESSION42", "")
SESSION43 = getenv("SESSION43", "")
SESSION44 = getenv("SESSION44", "")
SESSION45 = getenv("SESSION45", "")
SESSION46 = getenv("SESSION46", "")
SESSION47 = getenv("SESSION47", "")
SESSION48 = getenv("SESSION48", "")
SESSION49 = getenv("SESSION49", "")
SESSION50 = getenv("SESSION50", "")