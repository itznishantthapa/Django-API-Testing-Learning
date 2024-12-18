from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializers import FoodItemSerializers , FoodWithImageSerializers
from .models import FoodItem
# from django.contrib.auth.models import User

@csrf_exempt
@api_view(['POST','GET','PUT','DELETE'])
def createFoodItem(request,pk=None):
    if request.method == 'POST':
        owner = request.user.owner
        request.data['owner'] = owner.id  
        
        # Create the food item using the serializer
        serializer = FoodItemSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the food item
            return Response({"data": serializer.data, "msg": "Food Item Created Successfully"}, status=201)
        return Response({"msg": "Invalid Data", "errors": serializer.errors}, status=400)
        
    elif request.method == 'GET':
        owner = request.user.owner
        food_items=FoodItem.objects.filter(owner=owner)
        serializer=FoodItemSerializers(food_items,many=True)
        return Response({"data":serializer.data,"msg":"Food Items Fetched Successfully"},status=200)
    
    elif request.method=='PUT':
        food_item =FoodItem.objects.get(pk=pk)
        serializer=FoodItemSerializers(food_item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data,"msg":"Food Item Updated Successfully"},status=200)
        
    elif request.method=='DELETE':
        food_item =FoodItem.objects.get(pk=pk)
        food_item.delete()
        return Response({"msg":"Food Item Deleted Successfully"},status=200)



@csrf_exempt
@api_view(['POST'])
def createFoodWithImage(request):
    serializers=FoodWithImageSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response({"data":serializers.data,"msg":"Food Item with Image Created Successfully"},status=200)