from api.models import Category, Comment, Music, Person, Singer
from django.contrib import admin

# Register your models here.
admin.site.register(Music)
admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Singer)
