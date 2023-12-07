# Web Scraping with Aiogram and Celery Beat

## Overview

This project demonstrates web scraping using Aiogram for interacting with Telegram and Celery Beat for task scheduling. The goal is to take screenshots of a specific webpage, in this case, the "https://kun.uz/category/jahon" page.

## Features

- **Aiogram:** A powerful Python framework for developing Telegram bots.
- **Celery Beat:** A task scheduler built on top of Celery for periodic tasks.

## Requirements

- Python 3.x
- Aiogram
- Celery
- Other dependencies (check requirements.txt)

## Installation

1. Clone the repository:
  
        git clone https://github.com/your-username/your-repo.git
        cd your-repo
  
3. Install dependencies:

        pip install -r requirements.txt
  
4. Configure your Telegram API token in the `.env` file.

5. Configure other settings in the `.env` file as needed.

## Usage

1. Run the Celery worker:

        celery -A tasks worker --loglevel=info


2. Run the Celery Beat scheduler:

        celery -A tasks beat --loglevel=info

3. Run the main script:

        python main.py

The script will periodically take screenshots of the specified webpage and send them to your Telegram chat.

## Customization

- Adjust the schedule frequency in the `.env` file.
- Modify the webpage URL in the `main.py` file to target different pages.
- Customize the Telegram message content and recipients in the `tasks.py` file.

## Contributing

Feel free to contribute by opening issues or creating pull requests.
