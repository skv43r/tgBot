import uuid
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from config import TOKEN_API, on_startup


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_article(inline_query: types.InlineQuery):
    text = inline_query.query or 'Empty'
    input_content_bold = types.InputTextMessageContent(message_text=f'*{text}*',
                                                       parse_mode='markdown')
    input_content_italic = types.InputTextMessageContent(message_text=f'_{text}_',
                                                         parse_mode='markdown')
    item_bold = types.InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        input_message_content=input_content_bold,
        title='Botd',
        description=text,
        thumb_url='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/LetterB.svg/800px-LetterB.svg.png'
    )
    item_italic = types.InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        input_message_content=input_content_italic,
        title='Italic',
        description=text,
        thumb_url='https://cms-assets.tutsplus.com/cdn-cgi/image/width=850/uploads/users/2760/posts/41992/final_image/ItalicText_Final.jpg'
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item_bold, item_italic],
                                  cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
