from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/add')
b2 = KeyboardButton('/cancel')


kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)

kb_admin.row(b1, b2)
