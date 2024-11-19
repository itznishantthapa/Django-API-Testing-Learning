"""
URL configuration for TestDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from App1.views import createFoodItem, createFoodWithImage
from django.conf import settings
from django.conf.urls.static import static
from Owner.views import owner_data
from authentication.views import create_user

urlpatterns = [
    path('create_user/', create_user),
    path('admin/', admin.site.urls),
    path('createFoodItem/', createFoodItem),
    path('createFoodItem/<int:pk>/', createFoodItem), # This is for PUT request
    path('createFoodWithImage/', createFoodWithImage),
    path('owner_data/', owner_data),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
