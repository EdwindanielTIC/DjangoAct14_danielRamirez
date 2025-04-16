

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import logginForm, createUserForm


def index(request):
    return render(request, 'index.html')


def loggin_form(request):
    form = logginForm()

    if request.method == 'POST':
        form = logginForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {})

    context = {'form': form}
    return render(request, 'login.html', context)


def create_user(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'CreatUser.html', {'success': True})
    return render(request, 'CreatUser.html', {'form': form})


