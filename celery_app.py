from aiogram.types import Message, FSInputFile
from celery import Celery

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
    return data


celery.conf.beat_schedule = {
    'send_information_for_three_hours': {
        'task': 'celery_app.send_information_for_three_hours',
        'schedule': 10800.0
    }
}
