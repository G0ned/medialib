
from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #Esta clase se define para representar las opciones del campo "role" de la tabla usuarios.
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)
    def __str__(self):
        return self.username
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Platform(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Videogame(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    description = models.TextField(help_text='A brief description of the videogame.')
    categories = models.ManyToManyField(Category, verbose_name='videogame_category')
    platforms = models.ManyToManyField(Platform, verbose_name='videogame_platform', through='VideogamePlatform')
    def __str__(self):
        return self.title

class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videogames = models.ManyToManyField(Videogame, verbose_name='collection_videogame', through='VideogameCollection')
    def __str__(self):
        return f"{self.id}: {self.name}"

class VideogameCollection(models.Model):
    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

class VideogamePlatform(models.Model):
    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField(null=True, blank=True)
