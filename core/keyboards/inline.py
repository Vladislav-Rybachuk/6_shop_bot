from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

first_select = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Каталог',
            callback_data='catalog'
        )
    ],
    [
        InlineKeyboardButton(
            text='Корзина',
            callback_data='basket'
        )
    ],
    [
        InlineKeyboardButton(
            text='FAQ',
            callback_data='faq'
        )
    ]
])

second_select = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton(text='Футболки', callback_data='t_shirts'),
                                             InlineKeyboardButton(text='Шорты', callback_data='category_2')
                                         ],
                                         [
                                             InlineKeyboardButton(text='Рубашки', callback_data='category_3'),
                                             InlineKeyboardButton(text='Штаны', callback_data='category_4')
                                         ],
                                         [
                                             InlineKeyboardButton(text='категория 5', callback_data='category_5'),
                                             InlineKeyboardButton(text='категория 6', callback_data='category_6')
                                         ]
                                     ])

t_shirts = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Футболка 1', callback_data='t-shirt_1'),
                                        InlineKeyboardButton(text='Футболка 2', callback_data='t-shirt_2')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Футболка 3', callback_data='t-shirt_3'),
                                        InlineKeyboardButton(text='Футболка 4', callback_data='t-shirt_4')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Футболка 5', callback_data='t-shirt_5'),
                                        InlineKeyboardButton(text='Футболка 6', callback_data='t-shirt_6'),
                                        InlineKeyboardButton(text='Футболка 6', callback_data='t-shirt_6')
                                    ]
                               ])

product = InlineKeyboardMarkup(inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Добавить', callback_data='add'),
                                        InlineKeyboardButton(text='Количество',callback_data='quantity')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Корзина', callback_data='basket')
                                    ],
                                    [
                                        InlineKeyboardButton(text='<<Вернуться в  "Футболки"',callback_data='t_shirts')
                                    ]
                                ])


all_buttons = [
    InlineKeyboardButton(text='Футболка 1', callback_data='t-shirt_1'),
    InlineKeyboardButton(text='Футболка 2', callback_data='t-shirt_2'),
    InlineKeyboardButton(text='Футболка 3', callback_data='t-shirt_3'),
    InlineKeyboardButton(text='Футболка 4', callback_data='t-shirt_4'),
    InlineKeyboardButton(text='Футболка 5', callback_data='t-shirt_5'),
    InlineKeyboardButton(text='Футболка 6', callback_data='t-shirt_6'),
    InlineKeyboardButton(text='Футболка 7', callback_data='t-shirt_7'),
    InlineKeyboardButton(text='Футболка 8', callback_data='t-shirt_8')
]

def get_keyboard(page=0):
    buttons_per_page = 4
    start = page * buttons_per_page
    end = start + buttons_per_page
    current_buttons = all_buttons[start:end]

    # Добавить кнопки переключения
    navigation_buttons = []
    if page > 0:
        navigation_buttons.append(InlineKeyboardButton(text='⬅️ Назад', callback_data=f'page_{page-1}'))
    if end < len(all_buttons):
        navigation_buttons.append(InlineKeyboardButton(text='Вперед ➡️', callback_data=f'page_{page+1}'))

    # Создать клавиатуру
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.inline_keyboard = [current_buttons, navigation_buttons]

    return keyboard

@bot.callback_query_handler(func=lambda call: call.data.startswith('page_'))
def query_handler(call):
    page = int(call.data.split('_')[1])
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите футболку:", reply_markup=get_keyboard(page))

# all_buttons = [
#     InlineKeyboardButton(text='Кнопка 1', callback_data='button1'),
#     InlineKeyboardButton(text='Кнопка 2', callback_data='button2'),
#     InlineKeyboardButton(text='Кнопка 3', callback_data='button3'),
#     InlineKeyboardButton(text='Кнопка 4', callback_data='button4'),
#     InlineKeyboardButton(text='Кнопка 5', callback_data='button5'),
#     InlineKeyboardButton(text='Кнопка 6', callback_data='button6'),
#     InlineKeyboardButton(text='Кнопка 7', callback_data='button7'),
#     InlineKeyboardButton(text='Кнопка 8', callback_data='button8'),
# ]
#
# buttons_per_page = 4
# pagination = []
# current_page = 0
#
# for i in range(0, len(all_buttons), buttons_per_page):
#     page_buttons = all_buttons[i:i + buttons_per_page]
#     pagination.append(page_buttons)
#
#
# keyboard = InlineKeyboardMarkup(row_width=2, inline_keyboard=pagination[current_page])
#
# callback_data_next = 'next'
# callback_data_prev = 'prev'
#
# if current_page < len(pagination) - 1:
#     keyboard.add(InlineKeyboardButton(text='Вперед', callback_data=callback_data_next))
# if current_page > 0:
#     keyboard.add(InlineKeyboardButton(text='Назад', callback_data=callback_data_prev))



