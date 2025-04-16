from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.logginForm, name='login'),
    path('CreatUser', views.create_user, name='CreateUser'),

    # A continuacion creaaremos el path del boton que me llevara a CreateUser
    path('accion' , views.boton_CrearUsuario, name='CrearUsuario' ),
]