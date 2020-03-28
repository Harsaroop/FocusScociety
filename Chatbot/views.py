from django.shortcuts import render
from django.http import HttpResponse

def app1(request):
    return render(request, 'Chatbot/app1.html')

def index(request):
    return render(request, 'Chatbot/index.html')

def app2(request):
    return render(request, 'chatbot/app2.html')
