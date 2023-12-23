from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Task, Products
from .forms import TaskForm


def index(request):
    return render(request, 'main/index.html')


def news(request):
    return render(request, 'main/news.html')


def pro(request):
    product = Products.objects.all()
    return render(request, 'main/pro.html', {'product': product})


def about(request):
    return render(request, 'main/about.html')

def reviews(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/reviews.html', {'title': 'Отзывы', 'tasks': tasks})


def comment(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
        else:
            error = 'Форма была не верной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/comment.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('/admin/')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'main/login.html')


