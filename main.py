import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from core.handlers.basic import get_start, get_photo, get_hello
import asyncio
import django
import logging
from core.settings import settings
from aiogram.filters import ContentTypesFilter,Command, CommandStart
from aiogram import F
from core.utils.commands import set_commands
from core.handlers.callback import select_basket, select_catalog, select_faq, select_category_1, select_product_1
from core.handlers.pay import order, pre_checkout_query, successful_payment, shipping_check
#from aiogram.contrib.fsm_storage.memory import MemoryStorage

async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')

def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "django_project.telegrambot.telegrambot.settings"
    )
    #os.environ.update({"DJANGO_ALLOW_ASYNC_UNSAFE"": " True"})
    django.setup()


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')



async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                                "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    #storage = MemoryStorage()

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(order, Command(commands='pay'))
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment,ContentTypesFilter(content_types=[ContentType.SUCCESSFUL_PAYMENT]) ) #F.content_types.SUCCESSFUL_PAYMENT
    dp.shipping_query.register(shipping_check)
    dp.callback_query.register(select_basket, F.data.startswith('basket'))
    dp.callback_query.register(select_catalog, F.data.startswith('catalog'))
    dp.callback_query.register(select_category_1, F.data.startswith('t_shirts'))
    dp.callback_query.register(select_product_1, F.data.startswith('t-shirt_1'))
    dp.callback_query.register(select_faq, F.data.startswith('faq'))
    dp.message.register(get_hello, F.text =='Привет')
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_start, CommandStart())
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ =="__main__":
    setup_django()
    asyncio.run(start())
