import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message
import datetime
import datefinder
from google.oauth2 import service_account
from googleapiclient.discovery import build

with open('token.txt', 'r') as token:  # put your telegram bot token to 'token.txt'
    TOKEN = token.readline()

bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)
logger = logging.getLogger(__name__)


@dp.message_handler(commands={"start"})
async def command_start_handler(message: Message) -> None:
   await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")

@dp.message_handler(commands={"auth"})
async def command_auth_handler(message: Message) -> None:
   await message.answer("Soon, I'll authorize you to Google Calendar API")

@dp.message_handler(commands={"schedule"})
async def command_schedule_handler(message: Message) -> None:
   await message.answer(f"Soon I'll be able to add to Google Calendar entries")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

#git remote add origin https://github.com/xasanxon/google_calendar.git
