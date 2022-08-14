from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from aiogram import Bot, types
from misc import settings
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)


async def on_startup(dispatcher):
    await bot.set_webhook(settings.WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=settings.WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=settings.WEBAPP_HOST,
        port=settings.WEBAPP_PORT,
    )
