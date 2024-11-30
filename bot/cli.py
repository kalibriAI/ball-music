import asyncio
import logging

from aiogram.client.default import DefaultBotProperties
from colorama import Fore, init

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers.admin.admin_router import admin_router
from handlers.user.user_router import user_router

init(autoreset=True)
logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    print(Fore.GREEN + 'STATUS:', Fore.BLUE + "Starting bot")

    storage = MemoryStorage()

    # proxy_url = "http://proxy.server:3128" - прокси для pythonanywhere
    default_properties = DefaultBotProperties(parse_mode='html', link_preview_is_disabled=True)
    bot = Bot(token="7969398426:AAGPnBf_wn3Bw39seIn2Xhl3EzgE6ojxNi0", default=default_properties)
    dp = Dispatcher(storage=storage)

    dp.include_router(admin_router)
    dp.include_router(user_router)

    try:
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        await bot.session.close()


def cli():
    """Wrapper for command line"""
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")


# точка входа
if __name__ == '__main__':
    cli()
