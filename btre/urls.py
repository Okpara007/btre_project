"""
URL configuration for btre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  # can be linked to views or urls of another file, collecytion of your apps urls links
    path("", include("pages.urls")),
    path("listings/", include("listings.urls")),
    path("accounts/", include("accounts.urls")), # ensure you bring this into the main urls.py 
    path("contacts/", include("contacts.urls")), # after this you create the view method
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # enables media files to show up at the frontend 
