from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    password = models.CharField(max_length=128, null=False)

# he me visto obligado al hacer el python manage makemigration a escoger la opcion 1, esto me solicito una contraseña para todos los usuarios que sera 1234
    def __str__(self):
        return self.username