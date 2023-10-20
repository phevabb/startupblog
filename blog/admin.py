from django.contrib import admin
from .models import*

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'text', 'pub_date', ]
    prepopulated_fields = {'slug': ('title',)}
    list_filter =['tag', 'title', 'pub_date']
  #  list_editable = [ 'title', 'slug', 'text', 'startup', 'tag',]

# Register your models here.
