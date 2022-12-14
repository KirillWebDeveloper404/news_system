from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import CommandStart
from datetime import datetime
from loader import dp
from sql import User, Stat
from states import Anketa


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = User.get(User.tg_id == message.from_user.id)

        if user:
            await message.answer(f"Привет, {user.name}! \n" \
                "Это новостной бот, мы будем присылать тебе свежие новости")

    except User.DoesNotExist:
        new_user()
        await message.answer('Для начала заполните анкету')
        await message.answer('Пришлите ваш номер телефона(нажмите на кнопку)',
           reply_markup=ReplyKeyboardMarkup(
               [[
                    KeyboardButton('Отправить номер телефона', request_contact=True)
               ]], resize_keyboard=True)
           )
        await Anketa.phone.set()


@dp.message_handler(content_types=['contact'], state=Anketa.phone)
async def phone(message: types.Message):
    user = User()
    user.tg_id = message.from_user.id
    user.phone = message.contact['phone_number']
    user.name = message.from_user.full_name
    user.save()

    await message.answer('Как вас зовут', reply_markup=ReplyKeyboardRemove())
    await Anketa.name.set()


def new_user():
    date = datetime.today().strftime('%d.%m.%Y')

    try:
        stat = Stat.get(Stat.date == date)
        stat.count = str(int(stat.count) + 1)
        stat.save()
    except Stat.DoesNotExist:
        stat = Stat()
        stat.date = date
        stat.count = 1
        stat.save()
