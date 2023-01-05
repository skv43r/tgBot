from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

KB = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
button_1 = KeyboardButton('/help')
button_2 = KeyboardButton('/description')
#button_3 = KeyboardButton('❤️')
#button_4 = KeyboardButton('/minion')
button_5 = KeyboardButton('Random photo')
KB.add(button_5).add(button_1, button_2)

kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton('Random')
bp2 = KeyboardButton('Main menu')
kb_photo.add(bp1, bp2)

ikb = InlineKeyboardMarkup(row_width=2)
# ib1 = InlineKeyboardButton(text="Cooman",
#                            url='https://www.meme-arsenal.com/memes/f9cee52723ad3a8430bf0039a6979393.jpg')
# ikb.add(ib1)

ib2 = InlineKeyboardButton(text='👍', callback_data='like')
ib3 = InlineKeyboardButton(text='👎', callback_data='dislike')
ib4 = InlineKeyboardButton(text='Next', callback_data='next')
ib5 = InlineKeyboardButton(text='Main menu',callback_data='main')
ikb.add(ib2, ib3).add(ib4).add(ib5)