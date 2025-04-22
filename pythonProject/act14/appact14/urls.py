from django.urls import path,include
from . import views
urlpatterns = [
    path('login/', views.loggin_form, name='login'),

    path('create_user/', views.create_user, name='create_user'),
    path('PaginaLogin/', views.paginaIncial, name='paginaIncial'),

    path('cerrarSeccion/', views.cerrar_sesion, name='logout'),


]

# muy importante, el nombre path('PaginaLogin/'), tiene que ser el mismo nombre de la pagina web, si no
# no la va a encontrar