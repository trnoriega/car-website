from django.contrib import admin

from .models import Car, InputImage

class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'year', 'body_style']

admin.site.register(Car, CarAdmin)
admin.site.register(InputImage)
