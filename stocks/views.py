from django.shortcuts import render
import yfinance as yf
import pandas as pd
from . import config
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import os
from openai import OpenAI
from decouple import config




def stock_fundamentals_page(request):
    ticker = request.GET.get('ticker', 'AAPL')
    metric = request.GET.get('metric', 'info')
    
    stock = yf.Ticker(ticker)
    

    try:
        if metric == 'balance_sheet':
            data = stock.balance_sheet
        elif metric == 'income_statement':
            data = stock.financials
        elif metric == 'cash_flow':
            data = stock.cashflow
        elif metric == 'quarterly_financials':
            data = stock.quarterly_financials
        elif metric == 'recommendations':
            data = stock.recommendations
        elif metric == 'major_holders':
            data = stock.major_holders
        elif metric == 'institutional_holders':
            data = stock.institutional_holders
        elif metric == 'dividends':
            data = stock.dividends
            data = pd.DataFrame(data)
            data = data[::-1]
        elif metric == 'splits':
            data = stock.splits
        
            data = pd.DataFrame(data)
            data = data[::-1]
        
        else:
            data = stock.info
            data = pd.DataFrame.from_dict(data, orient='index')
            
    except Exception as e:
        data['error'] = str(e)
    
    return render(request, 'stocks/fundamentals.html', {'ticker': ticker, 'metric': metric, 'data': data})




# Initialize the OpenAI client
client = OpenAI(api_key=config('OPEN_AI_KEY'))

def generate_response(messages,model):
    try:
        response = client.chat.completions.create(
            model=model,  # You can change this to "gpt-4" if you have access
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

@api_view(['POST'])
def chat_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')
        model = data.get('model',config('GPT_MODEL'))
        user_id = request.POST.get('user_id')
        conversation = request.session.get(f'conversation_{user_id}', [
            {"role": "system", "content": "You are a helpful assistant."}
        ])
        
        conversation.append({"role": "user", "content": user_message})

        try:
            ai_response = generate_response(conversation,model)
            conversation.append({"role": "assistant", "content": ai_response})
            request.session['conversation'] = conversation
            return Response({"message": ai_response})
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=500)

    return Response({"message": "Invalid request method."}, status=400)

@api_view(['POST'])
def ask_ai_chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')
        metric = data.get('metric','')
        ticker = data.get('ticker','AAPL')
        user_id = request.POST.get('user_id')
        
        
        if ticker != "":
            stock = yf.Ticker(ticker)
            if metric == 'balance_sheet':
                data = stock.balance_sheet
            elif metric == 'income_statement':
                data = stock.financials
            elif metric == 'cash_flow':
                data = stock.cashflow
            elif metric == 'quarterly_financials':
                data = stock.quarterly_financials
            elif metric == 'recommendations':
                data = stock.recommendations
            elif metric == 'major_holders':
                data = stock.major_holders
            elif metric == 'institutional_holders':
                data = stock.institutional_holders
            elif metric == 'dividends':
                data = stock.dividends
                data = pd.DataFrame(data)
                data = data[::-1]
            elif metric == 'splits':
                data = stock.splits
            
                data = pd.DataFrame(data)
                data = data[::-1]
            elif metric == 'sustainability':
                data = stock.sustainability
            else:
                data = stock.info
                data = pd.DataFrame.from_dict(data, orient='index')
            
            user_message = f"{user_message} stock is {ticker} and the stock fundamental data is {data}"
            request.session[f'conversation_{user_id}'] = [{"role": "system", "content": "You are a helpful assistant."}]
        else:
            pass

        conversation = request.session.get(f'conversation_{user_id}', [
            {"role": "system", "content": "You are a helpful assistant."}
        ])
        
        conversation.append({"role": "user", "content": user_message})
        print(user_message)
        try:
            ai_response = generate_response(conversation,config('GPT_MODEL'))   #you can change this model to any model of your choice, it is the model which analyzes the stock data.
            conversation.append({"role": "assistant", "content": ai_response})
            request.session['conversation'] = conversation
            return Response({"message": ai_response})
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=500)

    return Response({"message": "Invalid request method."}, status=400)




def chatbot_view(request):
    return render(request, 'stocks/chatbot.html')

def ask_ai(request):
    return render(request, 'stocks/ask-ai.html')

def home(request):
    return render(request, 'stocks/home.html')