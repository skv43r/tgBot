from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from config import token, on_startup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


storage = MemoryStorage()
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)


class ProfileStatesGroup(StatesGroup):

    photo = State()
    name = State()
    age = State()
    gender = State()


def get_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/create'))
    return kb


def get_cancel_kb():
    ckb = ReplyKeyboardMarkup(resize_keyboard=True)
    ckb.add(KeyboardButton('/cancel'))
    return ckb


@dp.message_handler(commands=['cancel'], state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    if state is None:
        return
    await state.finish()
    await message.reply('You stopped process',
                        reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('Welcome, to create a profile type: /create',
                         reply_markup=get_kb())


@dp.message_handler(commands=['create'])
async def cmd_create(message: types.Message):
    await message.answer('Lets create your profile, to begin send me your photo',
                         reply_markup=get_cancel_kb())
    await ProfileStatesGroup.photo.set()


@dp.message_handler(lambda message: not message.photo, state=ProfileStatesGroup.photo)
async def check_photo(message: types.Message):
    await message.reply('This is not photo')


@dp.message_handler(content_types=['photo'], state=ProfileStatesGroup.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await message.reply('What is your name?')
    await ProfileStatesGroup.next()


@dp.message_handler(lambda message: not message.text.isdigit() or int(message.text) > 100, state=ProfileStatesGroup.age)
async def check_age(message: types.Message):
    await message.reply('Type your real age')


@dp.message_handler(state=ProfileStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.reply('How old are you?')
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.age)
async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await message.reply('What is your sex?')
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.gender)
async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=f"Name: {data['name']}\nAge: {data['age']}\nGender: {data['gender']}")
    await message.reply('Thank you')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
