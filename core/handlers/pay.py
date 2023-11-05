from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Покупка через Telegram бот',
        description='Лучший товар в лучшем магазине',
        payload='Оплата через Telegram бота',
        provider_token='381764678:TEST:69949',
        currency='rub',
        prices=[
            LabeledPrice(
                label='Оплата подписки',
                amount=99000,
            ),
            LabeledPrice(
                label='НДС',
                amount=20000,
            ),
            LabeledPrice(
                label='Скидка',
                amount=-20000,
            )
        ],
        max_tip_amount=5000,
        suggested_tip_amounts=[1000, 2000, 3000, 4000],
        start_parameter='Link',
        photo_url='https://smartfin.ua/uploads/blog_posts/9/249/image/c209b605463208fd232ccf9b09630825_detail.jpg',
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=False,
        reply_markup=None,
        request_timeout=15
    )

async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message):
    msg = f'Спасибо за оплату {message.successful_payment.total_amount // 100} {message.successful_payment.currency}.' \
          f'\r\n Наш менеджер получил заявку.'
    await message.answer(msg)
