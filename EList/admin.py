from django.contrib import admin
from .models import SignUp, Login, List, Item, Favorite, ArchiveAuthenticate, Archive
# Register your models here.

admin.site.register(SignUp)
admin.site.register(Login)
admin.site.register(List)
admin.site.register(Item)
admin.site.register(Favorite)
admin.site.register(ArchiveAuthenticate)
admin.site.register(Archive)