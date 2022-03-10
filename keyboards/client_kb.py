from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/schedule')
b2 = KeyboardButton('/adress')
b3 = KeyboardButton('/menu')
b4 = KeyboardButton('share number', request_contact=True)
b5 = KeyboardButton('my location', request_location=True)


kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

kb_client.row(b1, b2, b3).row(b4, b5)
#kb_client.add(b1).add(b2).insert(b3)
