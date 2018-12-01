from django.contrib import admin

# Register your models here.
from .models import Schedule, Cost, Album, Photo
from django.contrib.auth.models import User

# admin.site.unregister(User)
# admin.site.register(User)
admin.site.register(Schedule)
admin.site.register(Cost)
admin.site.register(Album)
admin.site.register(Photo)
