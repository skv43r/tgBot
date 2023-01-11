from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler, current_handler

from config import token

bot = Bot(token)
dp = Dispatcher(bot)
admin = 138483935


def set_key(key: str = None):

    def decorator(func):
        setattr(func, 'key', key)

        return func

    return decorator


class CheckMiddleWare(BaseMiddleware):

    async def on_process_callback_query(self, callback: types.CallbackQuery, data: dict):
        callback_id = callback.data[callback.data.find('_')+1:]
        if callback_id != str(callback.from_user.id):
            raise CancelHandler()


class AdminMiddleWare(BaseMiddleware):

    async def on_process_message(self, update: types.Update, data: dict):
        handler = current_handler.get()
        if handler:
            key = getattr(handler, 'key', 'Такого атрибута нет')
            print(key)


class FirstMiddleware(BaseMiddleware):

    async def on_pre_process_update(self, update: types.Update, data: dict):
        print('Pre process update')

    async def on_process_update(self, update: types.Update, data: dict):
        print('Process update')


@dp.message_handler(commands=['start'])
@set_key('yoyoyo')
async def cmd_start(message: types.Message):
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton('Кнопка', callback_data=f'check_{message.from_user.id}')]
    ])
    await message.answer('You write cmd start', reply_markup=ikb)
    print('Message')

@dp.callback_query_handler(lambda callback: callback.data.startswith('check_'))
async def cb_check(callback: types.CallbackQuery):
    await callback.message.answer('Ты жмякнул кнопку')

if __name__ == '__main__':
    dp.middleware.setup(CheckMiddleWare())
    executor.start_polling(dp,
                           skip_updates=True)