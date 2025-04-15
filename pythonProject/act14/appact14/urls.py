from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login_view, name='login'),
    path('inicio/', views.inicio_view, name='inicio'),
]