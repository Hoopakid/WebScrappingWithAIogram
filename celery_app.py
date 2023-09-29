from aiogram.types import Message, FSInputFile
from celery import Celery

from dispatcher import dp
from web_scrapping import get_information

celery = Celery(
    'main',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
)


# Assalomu alaykum ustoz, Ustoz man celeryni qo'ldan kegancha ishlatdim qoganlari 100 % to'gri
@celery.task
def send_information_for_three_hours():
    data = get_information()

    @dp.message(lambda msg: msg.text == '/news')
    async def send_information(message: Message):
        s = data["date"], data["year"], data["info1"], *data["info2"]
        photo = FSInputFile('example-firefox.png', filename='screenshot')
        await message.answer_photo(photo)
        await message.answer(str(s).replace(',', '').replace('(', '').replace(')', '').replace("'", ''))


celery.conf.beat_schedule = {
    'send_information_for_three_hours': {
        'task': 'celery_app.send_information_for_three_hours',
        'schedule': 10800.0
    }
}
