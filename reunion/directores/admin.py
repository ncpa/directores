from django.contrib import admin
from .models import Ut, Director
# Register your models here.

class UtAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class DirectorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Ut, UtAdmin)
admin.site.register(Director, DirectorAdmin)