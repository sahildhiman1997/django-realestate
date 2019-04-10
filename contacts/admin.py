from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','email','name','listing','dated')
    list_display_links=('id','name','listing')
    search_fields=('name','listing')
    list_per_page=25
admin.site.register(Contact, ContactAdmin)