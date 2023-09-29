import asyncio
import os

from aiogram import Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from dotenv import load_dotenv

from celery_app import send_information_for_three_hours
from dispatcher import dp

load_dotenv()


@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.answer(f"Hello {message.from_user.first_name}")
    await message.answer(f"Press /news to know about the latest information from the KUN UZ")


data = send_information_for_three_hours()


@dp.message(lambda msg: msg.text == '/news')
async def send_information(message: Message):
    s = data["date"], data["year"], data["info1"], *data["info2"]
    photo = FSInputFile('example-firefox.png', filename='screenshot')
    await message.answer_photo(photo)
    await message.answer(str(s).replace(',', '').replace('(', '').replace(')', '').replace("'", ''))


async def main():
    token = os.getenv('BOT_TOKEN')
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
