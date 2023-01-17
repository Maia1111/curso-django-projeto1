from django.contrib import admin

from .models import Category, Recipe


# Forma 1 de registrar no admin
class CategoryAdmin(admin.ModelAdmin):
    ...


# Forma 1 de registrar no admin
admin.site.register(Category, CategoryAdmin)


# Forma 2 de registra no admin usando decorate
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...
