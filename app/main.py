from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from aiogram import Bot, types
from misc import settings
from loguru import logger


bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)


async def on_startup(dispatcher):
    logger.info(f'start app:\n{settings.TOKEN=}\n{settings.WEBHOOK_URL=}\n{settings.WEBHOOK_PATH=}\n{settings.WEBAPP_HOST=}')
    await bot.set_webhook(settings.WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    logger.info('shutdown app')
    await bot.delete_webhook()


@dp.message_handler()
async def echo(message: types.Message):
    logger.debug(f'got message: {message.text}')
    await message.answer(message.text)


if __name__ == '__main__':
    try:
        start_webhook(
            dispatcher=dp,
            webhook_path=settings.WEBHOOK_PATH,
            skip_updates=True,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            host=settings.WEBAPP_HOST,
            port=settings.WEBAPP_PORT,
        )
    except Exception as main_exception:
        import sys
        logger.exception(main_exception)
        sys.exit()
