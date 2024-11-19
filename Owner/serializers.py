from rest_framework import serializers
from .models import Owner

class OwnerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Owner
        fields=['id','user','name','email','phone']