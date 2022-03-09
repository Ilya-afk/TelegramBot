import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from dotenv import load_dotenv

# load_dotenv() в данном случае и так работает, но это более общее решение
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
