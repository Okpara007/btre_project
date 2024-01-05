from django.contrib import admin

# Register your models here. after making the migrations you register the contact models so that we can see them in the admin area

from .models import Contacts # contacts here should have been in singular form 

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25

admin.site.register(Contacts, ContactAdmin)
