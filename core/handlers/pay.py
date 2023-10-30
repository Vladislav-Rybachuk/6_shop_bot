from aiogram import Bot
from aiogram.types import Message, LabeledPrice

async def order(message: Message, bot:Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Покупка через Telegram бот',
        description='1',
        provider_token='',
        currency='rub',
        prices=[
            LabeledPrice(
                'цена,скидка,ндс,бону'

            )
        ],
        max_tip_amount=,
        suggested_tip_
    )