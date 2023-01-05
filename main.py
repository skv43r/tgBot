# from aiogram import Bot, Dispatcher, executor, types
# from keyboards import KB, ikb
#
# TOKEN_API = "5933825181:AAFkb6ZS_VIlXclhB0qp-tPpSE83mMaHvfU"
#
# HELP_COMMAND = """
# <b>/start</b> - <em>Запуск бота</em>
# <b>/help</b> - <em>Список команд бота</em>
# <b>/description</b> - <em>Описание бота</em>
# <b>/minion</b> - <em>Получить фото mioion`a</em>
# """
#
# bot = Bot(TOKEN_API)
# dp = Dispatcher(bot)
#
# async def on_startup(_):
#     print("Бот запущен")
#
# @dp.message_handler(commands=['start'])
# async def start_command(message: types.Message):
#         await message.answer('<b>Ехала</b>',
#                              parse_mode='HTML',
#                              reply_markup=KB)
#
#
# @dp.message_handler(commands=['help'])
# async def help_command(message: types.Message):
#         await bot.send_message(message.from_user.id,
#                              text=HELP_COMMAND,
#                              parse_mode='HTML')
#
# @dp.message_handler(commands=['description'])
# async def help_command(message: types.Message):
#         await bot.send_message(message.from_user.id,
#                              text='Бот умеет отправлять id стикера',
#                              parse_mode='HTML')
#
# @dp.message_handler(commands=['minion'])
# async def send_minion(message: types.Message):
#         await bot.send_photo(chat_id=message.from_user.id,
#                              photo="https://static-cdn.jtvnw.net/jtv_user_pictures/cc393224-a3ec-4e97-bfdf-1aeb5c4ae863-profile_image-300x300.png")
#
# @dp.message_handler(content_types=['sticker'])
# async def sticker_id(message: types.Message):
#        await message.answer(message.sticker.file_id,
#                             reply_markup=ikb)
#
# @dp.message_handler()
# async def send_sticker(message: types.Message):
#     if message.text == '❤️':
#         await bot.send_sticker(chat_id=message.from_user.id,
#                                sticker='CAACAgIAAxkBAAOfY6y90jvyy97Te8RqE-Myb7zlbtgAAgQBAAJWnb0K3gTRemZm92wsBA')
#
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, on_startup=on_startup,)
#
from aiogram import Bot, Dispatcher, executor, types
from keyboards import KB, ikb, kb_photo
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
import random

TOKEN_API = "5933825181:AAFkb6ZS_VIlXclhB0qp-tPpSE83mMaHvfU"
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = '''
/start - Запуск бота
/help - Помощь 
/description - Описание бота  '''

photos = ['https://s0.rbk.ru/v6_top_pics/media/img/9/54/756709328571549.webp',
          'https://secretmag.ru/imgs/2021/12/27/13/5133072/8567053d43b6d6fc324d3c3806d3ca9ac54eec79.jpg',
          'https://www.rgo.ru/sites/default/files/styles/head_image_article/public/node/40899/ey-posony-saruman-uzhe-tochno-ne-pridyot-5.png?itok=uvfLDDcH',
          'https://i.pinimg.com/736x/15/e0/a3/15e0a381289ff16b808b545bb766aa94.jpg',
          'https://news.store.rambler.ru/img/c2375c436d119b62aeb38819b7117c20?img-format=auto&img-1-resize=height:355,fit:max&img-2-filter=sharpen']

diction = dict(zip(photos, ['Вкусно и точка', 'Симпл димпл нет попыт', 'Я сам не видел, но в орле и решке смотрел', 'Не зря на юрфаке учился', 'Вижу цель не вижу препятствий']))
random_photo = random.choice(list(diction.keys()))

flag = False

async def send_random(message: types.Message):
    random_photo = random.choice(list(diction.keys()))
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photo,
                         caption=diction[random_photo],
                         reply_markup=ikb)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="Ехала", reply_markup=KB)
    await message.delete()

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND)
    await message.delete()

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Бот отправляет фото, которое нужно оценить')
    await message.delete()

@dp.message_handler(Text(equals='Random photo'))
async def open_kb_photo(message: types.Message):
    await message.answer(text='Рандомная фотка',
                         reply_markup=ReplyKeyboardRemove())
    await send_random(message)
    await message.delete()

@dp.message_handler(Text(equals='Main menu'))
async def open_main_menu(message: types.Message):
    await message.answer(text='Вы находитесь в главном меню',
                         reply_markup=KB)

@dp.callback_query_handler()
async def callback_random_photo(callback: types.CallbackQuery):
    global random_photo
    global flag
    if callback.data == 'like':
        if not flag:
            await callback.answer("Вас рассмешнило 😂")
            flag = not flag
        else:
            await callback.answer('Вы уже лайкали')
    elif callback.data == 'dislike':
        await callback.answer('Согласен, не смешно 💩')
    elif callback.data == 'main':
        await callback.message.answer(text='Welcome to main menu',
                                      reply_markup=KB)
        await callback.message.delete()
        await callback.answer()
    else:
        random_photo = random.choice(list(filter(lambda x: x!= random_photo, list(diction.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                                           type='photo',
                                                           caption=diction[random_photo]),
                                          reply_markup=ikb)
        await callback.answer()

async def on_startup(_):
    print('Бот запустился')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)