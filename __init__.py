import asyncio
import logging
import sys
import time
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Any, Dict
from aiohttp import ClientSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from gpytranslate import Translator
from pyrogram import Client, filters, __version__, enums
from pytgcalls import GroupCallFactory
from .logging import *
from config import *
cmds = None
CMD_HELP = {}
clients = []
ids = []

SUDOERS = filters.user()
SUDO_USER = SUDOERS

AI = OPENAI_API
PM_LOGGER = PM_LOGGER

if BOTLOG_CHATID:
   BOTLOG_CHATID = BOTLOG_CHATID
else:
   BOTLOG_CHATID = "me"


SUDO_USER = SUDOERS
trl = Translator()
aiosession = ClientSession()
CMD_HELP = {}
scheduler = AsyncIOScheduler()
StartTime = time.time()
START_TIME = datetime.now()
TEMP_SETTINGS: Dict[Any, Any] = {}
TEMP_SETTINGS["PM_COUNT"] = {}
TEMP_SETTINGS["PM_LAST_MSG"] = {}

LOOP = asyncio.get_event_loop_policy()
event_loop = LOOP.get_event_loop()
asyncio.set_event_loop(event_loop)




class Bot(Client):
    def __init__(self):
        super().__init__(
            name="ubot",
            api_hash=API_HASH,
            api_id=API_ID,
            bot_token=BOT_TOKEN,
            workers=BOT_WORKERS,
            plugins=dict(root="Avengers/modules/bot"),
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Avengers stopped. Bye.")

class User(Client):
    def __init__(self):
        super().__init__(
            name="naya",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=USER_WORKERS,
            in_memory=True,
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
        )
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")


app = Bot()

if not BOT_TOKEN:
   LOGGER(__name__).error("WARNING: BOT TOKEN TIDAK DITEMUKAN, SHUTDOWN BOT")
   sys.exit()

bot1 = (
    Client(
        name="bot1",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION1,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION1
    else None
)

bot2 = (
    Client(
        name="bot2",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION2,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION2
    else None
)

bot3 = (
    Client(
        name="bot3",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION3,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION3
    else None
)

bot4 = (
    Client(
        name="bot4",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION4,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION4
    else None
)

bot5 = (
    Client(
        name="bot5",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION5,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION5
    else None
)
bot6 = (
    Client(
        name="bot6",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION6,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION6
    else None
)

bot7 = (
    Client(
        name="bot7",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION7,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION7
    else None
)

bot8 = (
    Client(
        name="bot8",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION8,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION8
    else None
)

bot9 = (
    Client(
        name="bot9",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION9,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION9
    else None
)

bot10 = (
    Client(
        name="bot10",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION10,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION10
    else None
)

bot11 = (
    Client(
        name="bot11",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION11,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION11
    else None
)

bot12 = (
    Client(
        name="bot12",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION12,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION12
    else None
)

bot13 = (
    Client(
        name="bot13",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION13,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION13
    else None
)

bot14 = (
    Client(
        name="bot14",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION14,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION14
    else None
)

bot15 = (
    Client(
        name="bot15",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION15,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION15
    else None
)

bot16 = (
    Client(
        name="bot16",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION16,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION16
    else None
)

bot17 = (
    Client(
        name="bot17",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION17,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION17
    else None
)

bot18 = (
    Client(
        name="bot18",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION18,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION18
    else None
)

bot19 = (
    Client(
        name="bot19",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION19,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION19
    else None
)

bot20 = (
    Client(
        name="bot20",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION20,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION20
    else None
)
bot21 = (
    Client(
        name="bot21",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION21,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION21
    else None
)

bot22 = (
    Client(
        name="bot22",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION22,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION22
    else None
)

bot23 = (
    Client(
        name="bot23",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION23,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION23
    else None
)

bot24 = (
    Client(
        name="bot24",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION24,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION24
    else None
)

bot25 = (
    Client(
        name="bot25",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION25,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION25
    else None
)

bot26 = (
    Client(
        name="bot26",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION26,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION26
    else None
)

bot27 = (
    Client(
        name="bot27",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION27,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION27
    else None
)

bot28 = (
    Client(
        name="bot28",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION28,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION28
    else None
)

bot29 = (
    Client(
        name="bot29",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION29,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION29
    else None
)

bot30 = (
    Client(
        name="bot30",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION30,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
        in_memory=True,
    )
    if SESSION30
    else None
)

bot31 = (
    Client(
        name="bot31",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION31,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION31
    else None
)

bot32 = (
    Client(
        name="bot32",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION32,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION32
    else None
)

bot33 = (
    Client(
        name="bot33",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION33,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION33
    else None
)

bot34 = (
    Client(
        name="bot34",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION34,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION34
    else None
)

bot35 = (
    Client(
        name="bot35",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION35,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION35
    else None
)

bot36 = (
    Client(
        name="bot36",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION36,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION36
    else None
)

bot37 = (
    Client(
        name="bot37",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION37,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION37
    else None
)

bot38 = (
    Client(
        name="bot38",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION38,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION38
    else None
)

bot39 = (
    Client(
        name="bot39",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION39,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION39
    else None
)

bot40 = (
    Client(
        name="bot40",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION40,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION40
    else None
)

bot41 = (
    Client(
        name="bot41",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION41,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION41
    else None
)

bot42 = (
    Client(
        name="bot42",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION42,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION42
    else None
)

bot43 = (
    Client(
        name="bot43",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION43,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION43
    else None
)

bot44 = (
    Client(
        name="bot44",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION44,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION44
    else None
)

bot45 = (
    Client(
        name="bot45",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION45,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION45
    else None
)
bot46 = (
    Client(
        name="bot46",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION46,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION46
    else None
)

bot47 = (
    Client(
        name="bot47",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION47,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION47
    else None
)

bot48 = (
    Client(
        name="bot48",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION48,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION48
    else None
)

bot49 = (
    Client(
        name="bot49",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION49,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION49
    else None
)

bot50 = (
    Client(
        name="bot50",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=SESSION50,
        workers=USER_WORKERS,
        plugins=dict(root="Avengers/modules"),
    )
    if SESSION50
    else None
)
  
bots = [bot for bot in [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10, bot11, bot12, bot13, bot14, bot15, bot16, bot17, bot18, bot19, bot20, bot21, bot22, bot23, bot24, bot25, bot26, bot27, bot28, bot29, bot30, bot31, bot32, bot33, bot34, bot35, bot36, bot37, bot38, bot39, bot40, bot41, bot42, bot43, bot44, bot45, bot46, bot47, bot48, bot49, bot50] if bot]

for bot in bots:
    if not hasattr(bot, "group_call"):
        setattr(bot, "group_call", GroupCallFactory(bot).get_group_call())
