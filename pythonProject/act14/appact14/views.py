from django.contrib.messages import success
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.hashers import make_password
from .forms import logginForm, createUserForm
from .models import Usuario


def index(request):
    return render(request, 'index.html')

# este sera lo que se recorrera el bucle
def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request,'CreatUser.html',{'usuarios':usuarios})


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
    success = False
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = createUserForm()

    return render(request, 'CreatUser.html', {'form': form, 'success': success})
    # esto hacer que me devuelva la web crearUsuario.hmtl, si no esta , no me la devuelve
