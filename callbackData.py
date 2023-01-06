from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from config import TOKEN_API, on_startup

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

cb = CallbackData('ikb', 'action')


ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Buton', callback_data='helo')]
])


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
