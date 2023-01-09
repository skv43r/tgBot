import hashlib
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from config import TOKEN_API, on_startup


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
user_data = ''


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text='Введите число')


@dp.message_handler()
async def text_handler(message: types.Message):
    global user_data
    user_data = message.text
    await message.reply(text='Ваши данные успешно сохранены')


@dp.inline_handler()
async def inline_echo(inline_query: types.inline_query):
    text = inline_query.query or 'Echo'
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    input_content = InputTextMessageContent(f'<b>{text}</b> - {user_data}',
                                            parse_mode='HTML')
    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title='Echo Bot',
        description='Эхо бот'
    )
    await bot.answer_inline_query(results=[item],
                                  inline_query_id=inline_query.id,
                                  cache_time=1)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
