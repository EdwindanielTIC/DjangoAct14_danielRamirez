from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)  # ID autogenerado
    username = models.CharField(max_length=50, unique=True)  # Campo único
    email = models.EmailField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return self.username