from .celery import app

#this makes sure anytime our project server is running, celery is starting too.
__all__ = ['app']