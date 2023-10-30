from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.inline import first_select


async def get_start(message: Message, bot:Bot):
    await bot.send_message(message.from_user.id, f'<b>Привет, {message.from_user.first_name}!</b>')
    await bot.send_photo(message.from_user.id,
                         photo='https://ecdn.teacherspayteachers.com/thumbitem/Welcome-to-my-store--4519208-1555593381/original-4519208-1.jpg',
                         caption='Добро пожаловать в наш магазин!',
                         reply_markup=first_select)
    chat_id = message.chat.id
    channel_username = 'chanel_username'# После указания канала нужно внести имя канала(без @)
    group_chat_id = 'group_chat_id'# Аналогично с группой group_chat_id
    try:
        result = await bot.get_chat_member(chat_id, channel_username)
        if result.status == "member" or result.status == "administrator" or result.status == "creator":
        # Пользователь подписан на канал
            await message.answer("Вы подписаны на наш канал!")
        else:
            # Пользователь не подписан на канал
            await message.answer("Подпишитесь на наш канал, чтобы продолжить!")

    except Exception as e:
        # Ошибка, возможно, канал не найден
        await message.answer("Произошла ошибка при проверке подписки на канал.")

    # Проверка вступления в группу
    try:
        result = await bot.get_chat_member(chat_id, group_chat_id)
        if result.status == "member" or result.status == "administrator" or result.status == "creator":
            # Пользователь является участником группы
            await message.answer("Вы участник нашей группы!")
        else:
            # Пользователь не является участником группы
            await message.answer("Присоединитесь к нашей группе, чтобы продолжить!")
    except Exception as e:
    # Ошибка, возможно, группа не найдена
        await message.answer("Произошла ошибка при проверке участия в группе.")

async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Отлично. Ты отправил картинку, я сохраню.')
    file = await bot.get_file((message.photo[-1].file_id))
    await bot. download_file(file.file_path,'photo.jpg')


async def get_hello(message: Message, bot: Bot):
    await message.answer(f'И тебе привет!')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)