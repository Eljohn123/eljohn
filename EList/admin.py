from django.contrib import admin
from .models import Login, Item, Favorite, Archive
# Register your models here.

admin.site.register(Login)
admin.site.register(Item)
admin.site.register(Favorite)
admin.site.register(Archive)