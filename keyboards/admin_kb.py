from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/add')
b2 = KeyboardButton('/cancel')
b3 = KeyboardButton('/delete')


kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)

kb_admin.row(b1, b3, b2)
