from aiogram import types, Router,F

routerReport = Router()

@routerReport.message(F.text.lower().startswith("rep1")) # отчет по одному офису
async def cmd_rep(message: types.Message):
    await message.answer(f"Вы ввели команду {message.text}")
