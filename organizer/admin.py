from django.contrib import admin
from .models import*

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name',)}
    list_filter =['name' ]
  #  list_editable = [ 'name', 'slug']
 #   list_display_links =['name']
# Register your models here.



def name(self):
    return self.name.upper()


@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):

    list_display = ['name', 'description', 'founded_date' , 'website']
    prepopulated_fields = {'slug': ('name',)}
    list_filter =['name' ]
    
    def uppercase_name(self, obj):
        return obj.name.upper()
    uppercase_name.short_description = 'Name'


