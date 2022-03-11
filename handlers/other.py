import json
import string
import hashlib

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle

from create_bot import dp


# @dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    text = query.query or 'echo'
    link = 'https://ru.wikipedia.org/wiki/'+text
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title='Статья Wiki',
        url=link,
        input_message_content=types.InputTextMessageContent(
            message_text=link))]

    await query.answer(articles, cache_time=1, is_personal=True)


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
    dp.register_inline_handler(inline_handler)
