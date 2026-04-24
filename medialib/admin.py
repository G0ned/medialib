from django.contrib import admin
from .models import User, Category, Platform, Videogame, Collection, VideogameCollection, VideogamePlatform

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Platform)
admin.site.register(Videogame)
admin.site.register(Collection)
admin.site.register(VideogameCollection)
admin.site.register(VideogamePlatform)