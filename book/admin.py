from django.contrib import admin

from .models import Recipe, Ingredient, Measurement

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Measurement)
