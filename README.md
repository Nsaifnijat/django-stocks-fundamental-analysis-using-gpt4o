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
Copygit clone https://github.com/Nsaifnijat/django-stocks-fundamental-analysis-using-gpt4o.git
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

Start the Redis server
--> redis-server
Start the Celery worker:
--> celery -A realtimeapp worker -l INFO
--> celery -A realtimeapp beat -l INFO
Run the Django development server:
--> python manage.py runserver  #you fundamental is upto date and realtime but the price that is displayed on the page might not appear, you can use the following command for that
--> daphne -p 8001 realtimeapp.asgi:application   #this can give the realtime price of stocks

API Usage
The project includes a RESTful API for stock data. You can access it at /api/stocks/.
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
