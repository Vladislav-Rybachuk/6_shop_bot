from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands  = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
        BotCommand(
            command='faq',
            description='FAQ'
        ),
        BotCommand(
            command='pay',
            description='Оплатить товары'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())