import json
import string

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import dp


# так можно избавиться от / и сделать более красиво
# @dp.message_handler(lambda message: 'пиво' in message.text)
async def beer(message: types.Message):
    await message.answer('ты в пиве')


# или так
# @dp.message_handler(Text(equals='аниме', ignore_case=True))
async def anime(message: types.Message):
    await message.answer('Твое имя')


# @dp.message_handler()
async def message_filter(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('black_list.json')))) != set():
        await message.reply('запрещенное слово!')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(beer, lambda message: 'пиво' in message.text.lower())
    dp.register_message_handler(anime, Text(equals='аниме', ignore_case=True))
    dp.register_message_handler(message_filter)
