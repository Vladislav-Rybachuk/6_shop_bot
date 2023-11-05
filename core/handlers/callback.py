from aiogram import Bot
from aiogram.types import CallbackQuery
from core.keyboards.inline import second_select, t_shirts, product


async def select_basket(call: CallbackQuery, bot: Bot):
    answer = f'Ваша Корзина ещё находится в разработке.'
    await call.message.answer(answer)
    await call.answer()


async def select_catalog(call: CallbackQuery, bot: Bot):
    await call.message.answer_photo(photo='https://cdn-user84060.skyeng.ru/uploads/6293a484a47a3784165045.png',
                                    caption="Выберите категорию из каталога:",
                                    reply_markup=second_select)
    await call.answer()


async def select_faq(call: CallbackQuery, bot: Bot):
    answer = f'Раздел FAQ находится в разработке.'
    await call.message.answer(answer)
    await call.answer()


async def select_category_1(call: CallbackQuery, bot: Bot):
    await call.message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiefpACH2VwCcdUH4xAvp0eZQHHZP-2Cu-FQ&usqp=CAU',
                                    caption='Выберите товар из категории "Футболки"',
                                    reply_markup=t_shirts)
    await call.answer()


async def select_product_1(call: CallbackQuery, bot: Bot):
    await call.message.answer_photo(photo='https://content1.rozetka.com.ua/goods/images/big/277910331.jpg',
                                    caption=f'Футболка чёрная. Размер L. Цена 10',
                                    reply_markup=product)
    await call.answer()
