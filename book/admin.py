from django.contrib import admin

from .models import Recipe, Ingredient, Measurement, Icon, Note

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Measurement)
admin.site.register(Icon)
admin.site.register(Note)
