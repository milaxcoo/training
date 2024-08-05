import sqlite3

from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from crud_functions import initiate_db, get_all_products

api = "7248785286:AAFZ47NdkM4_oBuNVYdC8-ZBXvzgwCrYwHs"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

initiate_db()


def populate_products():
    connection = sqlite3.connect('database_tg.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Products (title, description, price) VALUES ('Котик 1', 'Прикольный котик', 100)")
    cursor.execute("INSERT INTO Products (title, description, price) VALUES ('Котик 2', 'Забавный котик', 200)")
    cursor.execute("INSERT INTO Products (title, description, price) VALUES ('Котик 3', 'Милашка котик', 300)")
    cursor.execute("INSERT INTO Products (title, description, price) VALUES ('Котик 4', 'Крутой котик', 400)")

    connection.commit()
    connection.close()


# populate_products()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


def get_keyboard():
    buttons = [
        KeyboardButton(text='Рассчитать'),
        KeyboardButton(text='Информация'),
        KeyboardButton(text='Купить')
    ]
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    return keyboard


def get_inline_product_keyboard():
    buttons = [
        InlineKeyboardButton(text='Котик 1', callback_data='product_buying'),
        InlineKeyboardButton(text='Котик 2', callback_data='product_buying'),
        InlineKeyboardButton(text='Котик 3', callback_data='product_buying'),
        InlineKeyboardButton(text='Котик 4', callback_data='product_buying')
    ]
    inline_keyboard = InlineKeyboardMarkup()
    inline_keyboard.add(*buttons)
    return inline_keyboard


def get_inline_keyboard():
    buttons = [
        InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
        InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
    ]
    inline_keyboard = InlineKeyboardMarkup()
    inline_keyboard.add(*buttons)
    return inline_keyboard


@dp.message_handler(commands=['start'])
async def start(message):
    keyboard = get_keyboard()
    await message.reply("Добро пожаловать! Выберите опцию:", reply_markup=keyboard)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()

    photos = [
        "https://image.petmd.com/files/styles/978x550/public/2023-09/how-smart-are-cats.jpg",
        "https://sussexbylines.co.uk/wp-content/uploads/2024/03/cat-out-hunting.jpg",
        "https://www.forbes.com/advisor/wp-content/uploads/2023/09/getty_creative.jpeg-900x510.jpg",
        "https://humanepro.org/sites/default/files/styles/article_new/public/images/post/cat-portrait.jpg?itok=36RD2Zba"
    ]

    for product, photoo in zip(products, photos):
        description = f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}"
        await message.reply(description)
        await bot.send_photo(message.chat.id, photo=photoo)

    inline_keyboard = get_inline_product_keyboard()
    await message.reply("Выберите продукт для покупки:", reply_markup=inline_keyboard)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    inline_keyboard = get_inline_keyboard()
    await message.reply("Выберите опцию:", reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.reply("Вы успешно приобрели продукт!")
    await call.answer()


@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula_text = (
        "Формула Миффлина - Сан Жеора для мужчин:\n"
        "BMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (г) + 5\n\n"
        "Формула для женщин:\n"
        "BMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (г) - 161"
    )
    await call.message.reply(formula_text)
    await call.answer()


@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.reply('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.reply('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.reply('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Формула Миффлина - Сан Жеора для мужчин
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.reply(f"Ваша дневная норма калорий: {calories} ккал.")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
