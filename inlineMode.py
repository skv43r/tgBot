import hashlib

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from config import TOKEN_API, on_startup
from aiogram.utils.callback_data import CallbackData


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
cb = CallbackData('ikb', 'action')


def get_ikb():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Button1', callback_data=cb.new('push_1')),
         InlineKeyboardButton(text='Button2', callback_data=cb.new('push_2'))]
    ])
    return ikb


@dp.callback_query_handler(cb.filter(action='push_1'))
async def push_first(callback: types.CallbackQuery):
    await callback.answer('Hello')


@dp.callback_query_handler(cb.filter(action='push_2'))
async def push_second(callback: types.CallbackQuery):
    await callback.answer('World')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text='Welcome to Bot',
                         reply_markup=get_ikb())


@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery):
    text = inline_query.query or 'Echo'
    if text == 'photo':
        input_content = InputTextMessageContent('This is a photo')
    else:
        input_content = InputTextMessageContent(text)
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title='Inline Message'
    )
    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item],
                                  cache_time=1)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
