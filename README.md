# django-stocks-fundamental-analysis-using-gpt4o
Django Stock Fundamental Analysis using GPT MODELS and  Chatbot
Overview
This project includes two apps a chatbot and a realtime stocks fundamental analysis with GPT4o, the realtime analysis app is a Django-based web application for performing fundamental analysis on stocks. It leverages real-time financial data and provides a user-friendly interface for analyzing stock performance and fundamentals.
Features

Real-time stock data fetching using yfinance
Asynchronous task processing with Celery
Real-time updates using Django Channels
RESTful API for stock data retrieval
Chatbot for other tasks.

Technologies Used

Django 5.0.6
Celery 5.4.0
Channels 4.1.0
Daphne 4.1.2
Django REST Framework 3.15.2
yfinance 0.2.40

Prerequisites

Python 3.x
Redis (for Channels and Celery)

Installation

Clone the repository:
git clone https://github.com/Nsaifnijat/django-stocks-fundamental-analysis-using-gpt4o.git
cd django-stocks-fundamental-analysis-using-gpt4o

Create a virtual environment and activate it:
Copypython -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:
brew/pip install -r requirements.txt

Set up the database:
python manage.py migrate

Create a superuser (optional):
python manage.py createsuperuser


Running the Application

# Start the Redis server
# Redis is used for caching and as a message broker for Celery
redis-server

# Start the Celery worker
# This processes background tasks for your application
celery -A realtimeapp worker -l INFO

# Start the Celery beat scheduler
# This is used for scheduling periodic tasks
celery -A realtimeapp beat -l INFO

# Run the Django development server
# This starts your main application server
# Note: Fundamental analysis will be up-to-date, but stock prices might not update in real-time
python manage.py runserver

# (Optional) Run the application using Daphne for real-time price updates
# This enables WebSocket connections for live stock price updates
daphne -p 8001 realtimeapp.asgi:application



#create a .env file and have the following secrets saved. put your own keys
OPEN_AI_KEY = 'sk-nnnnnnn'
DJANGO_SECRET_KEY = "django-insecure-tjjjksjx"
GPT_MODEL =  "gpt-4o"




API Usage
The project includes a RESTful API for stock data. You can access it at /api/stocks/.
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
