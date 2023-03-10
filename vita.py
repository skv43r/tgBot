from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio


TOKEN_API = '5889381554:AAFpRvAcLnmUZ8D6EOweUcoGnL_UADqyGoQ'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


text = ['Витоша, я очень сильно тебя лублу и скучаю',
        'Ты – лучик моего солнца',
        'Ты всегда меня поддерживаешь, чтобы не случилось',
        'Я невероятно ценю то что ты есть у меня',
        'Ты – уникальная',
        'Прекрасней тебя нет никого на свете',
        'Ты – очень талантливая и креативная',
        'Ты являешься примером того, к чему нужно стремиться',
        'Ты вдохновляешь людей заниматься бизнесом',
        'У тебя отлично получается вести блог и помогать людям',
        'Рядом с тобой я чувствую себя самым счастливым на свете',
        'Я благодарен за то, что ты у меня есть',
        'Когда мне грустно, одна только мысль о тебе поднимает настроение',
        'Я соскучился и просто хотел поднять тебе настроение, сказать о том как сильно я тебя люблю ❤️']

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Нажми на меня!!', callback_data='button')]])

flag = False


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text='Привет <b>Виточка</b>, этот бот я написал для тебя',
                         parse_mode='HTML',
                         reply_markup=ikb)
    await message.delete()


@dp.callback_query_handler(text='button')
async def btn(callback: types.CallbackQuery):
    global flag
    await callback.message.delete()
    if not flag:
        flag = not flag
        i = 0
        while i < len(text):
            await asyncio.sleep(1800)
            await callback.message.answer(text=text[i])
            i += 1
    await callback.answer('Кнопка уже нажата', show_alert=True)


async def on_startup(_):
    print('Bot in progress')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)