from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.

# 검색


def index(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        print(todos)
        return render(request, 'todo/index.html', {"todos": todos})
    else:
        return HttpResponse("invalid request method", status="405")


def read(request, todo_id):
    content = Todo.objects.get(id=todo_id)
    print(content)
    return render(request, 'todo/detail.html', {'content': content})

# 삽입


@login_required(login_url="/user/sign-in/")
@csrf_exempt
def create(request):
    if request.method == "POST":
        Todo.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            user=request.user,
            image=request.FILES.get("image"),
        )

        return redirect('/todo/')

    elif request.method == "GET":
        return render(request, 'todo/create.html')
    else:
        return HttpResponse("invalid request mothod", status="405")

# 삭제


@csrf_exempt
def delete(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(id=todo_id)
        if request.user == todo.user:
            todo.delete()
            return redirect('/todo/')
        else:
            return HttpResponse("Yout are not allowed to delete this todo", status="403")
    else:
        return HttpResponse("valid request method", status="405")

# 갱신


def update(request, todo_id):
    if request.method == "POST":
        if request.user == content.user:
            todo = Todo.objects.get(id=todo_id)
            todo.content = request.POST['update']
            todo.save()
            return redirect(f"/todo/{todo_id}/")
        else:
            return HttpResponse("Yout are not allowed to delete this todo", status="403")
    elif request.method == "GET":
        content = Todo.objects.get(id=todo_id)
        return render(request, 'todo/update.html', {'content': content})
    else:
        return HttpResponse("invalid request method", status="405")
