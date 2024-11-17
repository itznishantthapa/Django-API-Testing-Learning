from rest_framework import serializers
from .models import FoodItem, FoodWithImage

class FoodItemSerializers(serializers.ModelSerializer):
    class Meta:
        model=FoodItem
        fields=['id','name','price','description']


class FoodWithImageSerializers(serializers.ModelSerializer):
    class Meta:
        model=FoodWithImage
        fields=['id','image','name']