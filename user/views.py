from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .models import User
# Create your views here.


@csrf_exempt
def signup(request):
    if request.method == "GET":
        return render(request, "user/signup.html")
    elif request.method == "POST":
        User.objects.create_user(
            username=request.POST['id'], password=request.POST['pw'])
        return redirect("/todo/")
    else:
        return HttpResponse("invalid request method", status="405")


def signin(request):
    if request.method == "POST":
        username = request.POST['id']
        password = request.POST['pw']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/todo/')
        else:
            return HttpResponse("invalid auth", status="401")
    elif request.method == "GET":
        return render(request, "user/signin.html/")
    else:
        return HttpResponse("invalid request method", status="405")


def signout(request):
    logout(request)
    return redirect('/todo/')
