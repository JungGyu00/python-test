from django.http import HttpResponse
from django.shortcuts import render


def pingpong(request):
    print(request.headers)
    return render(request, 'pong.html')


def index(request):
    print(request.GET.get('name'))
    name = request.GET.get('name')
    return render(request, 'index.html', {'name': name})


def getdata(request):
    print(request.POST.get('to-do'))
    return HttpResponse('GetData')
