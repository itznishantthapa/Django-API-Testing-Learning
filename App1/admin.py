from django.contrib import admin
from .models import FoodItem,FoodWithImage
# Register your models here.

admin.site.register(FoodItem)
admin.site.register(FoodWithImage)