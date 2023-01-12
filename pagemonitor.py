import requests
from bs4 import BeautifulSoup

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import token, on_startup

bot = Bot(token)
dp = Dispatcher(bot)

url = 'https://geekstand.top/development/python-beautifulsoup-parsim-odnotipnye-jelementy-veb-stranicy/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find(class_='site-navigation ast-flex-grow-1 navigation-accessibility site-header-focus-item')
check_items = content.findAll(class_='menu-link')


def page_monitor():
    while True:
        for item in check_items:
            text = item.find(class_='menu-text').text
            name = str(text).replace(' ', '_').lower()
            print(f"<string name=\'{name}\'>{text}</string>")
        if text != text:
            text = item.find(class_='menu-text').text
            name = str(text).replace(' ', '_').lower()
            print(f"<string name=\'{name}\'>{text}</string>")
        return text


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('Бот будет отслеживать изменения на заданной странице')
    await bot.send_message(chat_id=message.from_user.id, text=page_monitor())


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)