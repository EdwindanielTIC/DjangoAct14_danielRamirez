from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

from .forms import createUserForm
from .models import Usuario



def paginaIncial(request):
    return render(request, 'PaginaLogin.html')

# este sera lo que se recorrera el bucle
def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request,'CreatUser.html',{'usuarios':usuarios})


def loggin_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Usuario.objects.get(username=username)
            if check_password(password, user.password):
                request.session['usuario_id'] = user.id
                return redirect('paginaIncial')
            else:
                error = 'Contraseña incorrecta'
        except Usuario.DoesNotExist:
            error = 'Usuario no encontrado'

        return render(request, 'login.html', {'error': error})

    return render(request, 'login.html')


# voy a crear una vista para que cunado cierre la sección , me lleve devulta al inicio de sedccion
def cerrar_sesion(request):
    logout(request)
    return redirect('login')

def create_user(request):
    success = False
    if request.method == 'POST':
        form = createUserForm(request.POST)
        # el siguiente es muy imporante, porque antes estaba pasando el formulario de login
        # pero sin pasar nunca por el make_password(), esto significa que se me guardbaa en la base de datos la contraseña
        # en texto plano y luego el check_password() no me la podia validar.
        # otro problema mas que tenia era que estaba inciando seccion con usuario que no tenian la contraseña cifrada y esto
        # me probocaba no poder iniciar seccion, una vez puesto el make_password() y check_password() todo funciona bieN
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.password = make_password(form.cleaned_data['password'])  # Cifrar contraseña si no no me deja, PUNTO MUY IMPORTANTE
            usuario.save()
            success = True
    else:
        form = createUserForm()

    return render(request, 'CreatUser.html', {'form': form, 'success': success})