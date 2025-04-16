from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import logginForm, createUserForm


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


def create_user(request):
    form = createUserForm()

    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'CreatUser.html', {'success': True})
    # return render(request, 'CreatUser.html', {'form': form})

# funcion que me creara el boton para ir a la creacion de usuario y contraseña

def boton_CrearUsuario(request):
     return render(request, 'CreatUser.html' )
