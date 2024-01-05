from django.db import models
from datetime import datetime

# Create your models here. first thing that was done
class Contacts(models.Model): # The contacts here should have been changed to singular form to avoid errors in the admin area
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True) # means it is optional ie it can be empty
    contact_date = models.DateTimeField(default=datetime.now, blank=True) # to use datetime.now you need to import it
    user_id = models.IntegerField(blank=True) # set because someone who isn't logged in can also make an inquiry, however if logged in we want to track the user_id
    def __str__(self):
        return self.name # main field we are refering to. After this we would want to create a table in the database for our contacts so we need to create migrations (in the terminal), but ensure to put new app inside installed apps first
