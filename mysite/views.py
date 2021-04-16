from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    values = {'name':'Akshay Shelar', 'age':24, 'city':'Aurangabad','college':'CSMSS'}
    return render(request, 'home.html', values)