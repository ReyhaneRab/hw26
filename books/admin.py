from django.contrib import admin
from books.models import *

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'recommendedby', 'popularity_score']


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'publisher']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'recommendedby', 'joindate', 'popularity_score']


