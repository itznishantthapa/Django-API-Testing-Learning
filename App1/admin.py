from django.contrib import admin
from .models import FoodItem,FoodWithImage


admin.site.register(FoodItem)
admin.site.register(FoodWithImage)