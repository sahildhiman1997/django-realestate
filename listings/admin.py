from django.contrib import admin
from .models import Listing
# Register your models here.

class AdminListing(admin.ModelAdmin):
    list_display=('id','title','published','realtor')
    list_display_links=('id','title')
    list_filter=('realtor',)
    list_editable=('published',)

admin.site.register(Listing, AdminListing)