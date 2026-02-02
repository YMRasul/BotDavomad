from HandStart import GetrouterStart
from HandAdmin import GetRouterAdmin
from HandHelp import routerHelp
from HandReport import routerReport
import asyncio
import logging
from dbase import dbase_start
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from config import TOKEN

async def on_startup():
    await bot.send_message(chat_id=139204666, text='Бот запущен!')
    await dbase_start()
    print("Бот запущен!")

async def on_shutdown():
    print('Остановка Бота.')
    await bot.send_message(chat_id=139204666, text='Бот остановлен!')
    # Удаляем вебхук и, при необходимости, очищаем ожидающие обновления
    await bot.delete_webhook(drop_pending_updates=True)
    # Закрываем сессию бота, освобождая ресурсы
    await bot.session.close()

async def main():                       # Запуск процесса поллинга новых апдейтов
    routerStart = GetrouterStart(bot)
    dp.include_router(routerStart)      # 1. Start hendler

    routerAdmin = GetRouterAdmin(bot)
    dp.include_router(routerAdmin)  # 2. Admin hendler

    dp.include_router(routerReport)
    dp.include_router(routerHelp)

    dp.startup.register(on_startup)    # регистрация функцию  on_startup()
    dp.shutdown.register(on_shutdown)  # регистрация функцию  on_shutdown()

    await bot.delete_webhook(drop_pending_updates=True)

    try:
        # Удаляем вебхуки и запускаем поллинг
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        # ВАЖНО: Закрываем сессию бота при выходе
        await bot.session.close()
# ----------------------------------------------------------------------------------------------
bot = Bot(token=TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML))   # тут ещё много других интересных настроек
dp = Dispatcher()      # Диспетчер
# Включаем логирование, чтобы не пропустить важные сообщения. При  Production, это не желательно
#logging.basicConfig(level=logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    format=u'%(levelname)-8s [%(asctime)s] %(message)s'
)
# Это для без аврийного остановки Бота при нажатие    Cntrl <C>
try:
    print('Запуск бота!')
    asyncio.run(main())
except KeyboardInterrupt:
    print('Бот остановлен!')
#
#