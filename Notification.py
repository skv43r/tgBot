from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from config import TOKEN_API
import asyncio
from notifiers import get_notifier
import time

token = '5430038322:AAGdHoY2ECrlDmqlTM2i1xVJXx3J_wS2KTc'
bot = Bot(token)
dp = Dispatcher(bot)


async def on_startup():
    user_should_be_notified = 138483935
    await bot.send_message(user_should_be_notified, 'Бот запущен')


if __name__ == '__main__':
    executor.start(dp, on_startup())
    executor.start_polling(dp, skip_updates=True)

