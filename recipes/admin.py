from django.contrib import admin

from .models import Category, Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published', 'category', 'author',
                    'created_at', 'updated_at']

    list_display_links = ('id', 'title', 'is_published')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at',
                    'updated_at']
