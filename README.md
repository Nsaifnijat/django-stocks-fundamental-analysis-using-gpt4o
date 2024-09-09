# Django Stock Fundamental Analysis using GPT Models and Chatbot

## Overview

This project comprises two main applications:
1. A chatbot for various tasks
2. A real-time stocks fundamental analysis tool using GPT models

The real-time analysis app is a Django-based web application that performs fundamental analysis on stocks. It leverages real-time financial data and provides a user-friendly interface for analyzing stock performance and fundamentals.

## Features

- Real-time stock data fetching using yfinance
- Asynchronous task processing with **Celery**
- Real-time updates using **Django Channels**
- RESTful API for stock data retrieval
- Chatbot for other tasks
- Integration with GPT models for advanced analysis

## Technologies Used

### Backend
- Django 5.0.6
- **Celery 5.4.0**
- **Django Channels 4.1.0**
- Daphne 4.1.2
- Django REST Framework 3.15.2
- yfinance 0.2.40
- Python 3.x

### Frontend
- HTML
- JavaScript
- Tailwind CSS

### Other
- **Redis** (for Channels and Celery)

## Prerequisites

- Python 3.x
- Redis

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Nsaifnijat/django-stocks-fundamental-analysis-using-gpt4o.git
   cd django-stocks-fundamental-analysis-using-gpt4o
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   python manage.py migrate
   ```

5. (Optional) Create a superuser:
   ```
   python manage.py createsuperuser
   ```

## Configuration

Create a `.env` file in the project root and add the following secrets:

```
OPEN_AI_KEY = 'sk-your-openai-key'
DJANGO_SECRET_KEY = "your-django-secret-key"
GPT_MODEL = "gpt-4o"
```

Replace the placeholder values with your actual keys.

## Running the Application

1. Start the Redis server:
   ```
   redis-server
   ```

2. Start the Celery worker:
   ```
   celery -A realtimeapp worker -l INFO
   ```

3. Start the Celery beat scheduler:
   ```
   celery -A realtimeapp beat -l INFO
   ```

4. Run the Django development server:
   ```
   python manage.py runserver
   ```

   Note: Fundamental analysis will be up-to-date, but stock prices might not update in real-time.

5. (Optional) For real-time price updates, run the application using Daphne:
   ```
   daphne -p 8001 realtimeapp.asgi:application
   ```



## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
##Contact
Email: aithequant@gmail.com

