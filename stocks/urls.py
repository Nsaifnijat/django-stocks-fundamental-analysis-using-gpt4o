from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fundamentals/', views.stock_fundamentals_page, name='stock-fundamentals'),
    path('chat/',views.chatbot_view,name='chatbot'), # this chatbot, chats with Openai Models
    path('api/chat/',views.chat_api,name='api-call'),
    path('api/ask/',views.ask_ai,name='ask-ai'),
    path('api/ask/chat/', views.ask_ai_chat, name='ask-ai-chat'),
    # Add other URLs as needed
]
