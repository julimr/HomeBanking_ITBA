from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=20)
    email = models.EmailField(max_length = 50)

class Login(models.Model):
    username = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length = 50)