from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="listings"), # first parameter(root path/home page), second parameter(mathod that we want to connect it to), final parameter(the name which would be used to easily access the path)
    path('<int:listing_id>', views.listing, name="listing"),
    path('search', views.search, name="search")
]