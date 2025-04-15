from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import logginForm

def index(request):
    return render(request, 'index.html')


def login_view(request):
    return render(request, 'login.html', {})


def loggin_form(request):
    form = logginForm()

    if request.method == 'POST':
        form = logginForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {})

    context = {'form': form}
    return render(request, 'login.html', context)

