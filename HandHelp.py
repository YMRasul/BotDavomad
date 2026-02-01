from aiogram import Router,F
from config import superadmin,DBASE
from aiogram.filters import Command
#----------------------------
routerHelp = Router()
#----------------------------
@routerHelp.message(Command('help'))
async def copybase(message):
    hlp = ''
    if message.from_user.id == superadmin:  # superUser
        hlp = hlp + "\n/copy\n/copybase\n/copylog\n/droplog"
        await message.answer(hlp)
