from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def app1(request):
    return render(request, 'app1.html')

def app2(request):
    return render(request, 'app2.html')