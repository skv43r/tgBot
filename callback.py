from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN_API, on_startup

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

is_vote = False

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='like', callback_data='like'),
     InlineKeyboardButton(text='dislike', callback_data='dislike')],
    [InlineKeyboardButton(text='Close keyboard', callback_data='close')]])


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://static-cdn.jtvnw.net/jtv_user_pictures/cc393224-a3ec-4e97-bfdf-1aeb5c4ae863-profile_image-300x300.png',
                         caption='Зацени',
                         reply_markup=ikb)
    await message.delete()


@dp.callback_query_handler(text='close')
async def ikb_close(callback: types.CallbackQuery):
    await callback.message.delete()


@dp.callback_query_handler()
async def btn_dislike(callback: types.CallbackQuery):
    global is_vote
    if not is_vote:
        if callback.data == 'like':
            await callback.answer(text='123')
            is_vote = not is_vote
        else:
            await callback.answer(text='456')
            is_vote = not is_vote
    await callback.answer("voted")


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
