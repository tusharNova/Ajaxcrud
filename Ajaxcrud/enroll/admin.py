from django.contrib import admin

from .models import User,infodata

# Register your models here.

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')

@admin.register(infodata)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')