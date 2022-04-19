from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def pag1(request):
    return render(request, 'core/pag1.html')