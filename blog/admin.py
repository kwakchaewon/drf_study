from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    list_display_links= ['username', 'email']


@admin.register(BoardCategories)
class BoardCategoriesAdmin(admin.ModelAdmin):
    list_display = ['category_type', 'category_code', 'category_name']
    list_display_links= ['category_type', 'category_code', 'category_name']


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['title', 'conntents', 'user', 'created_date']
    list_display_links= ['title', 'conntents']


@admin.register(BoardReplies)
class BoardRepliesAdmin(admin.ModelAdmin):
    list_display = ['contents', 'user', 'created_date']
    list_display_links= ['contents']


@admin.register(BoardLikes)
class BoardLikesAdmin(admin.ModelAdmin):
    list_display = ['board', 'user', 'created_date']
    list_display_links= ['board', 'user', 'created_date']
