from django.shortcuts import render

def home(request):
    return render(request, 'photoplanet/index.html')

def all(request):
    return render(request, 'photoplanet/all.html')

def about(request):
    return render(request, 'photoplanet/about.html')

def login(request):
    return render(request, 'photoplanet/login.html')

def day(request):
    return render(request, 'photoplanet/day.html')