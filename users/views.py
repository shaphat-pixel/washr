from django.shortcuts import render
from .models import *

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required 
from rest_framework.decorators import api_view
from .serializers import *
from . models import *
# Create your views her


#@login_required
@api_view(['GET'])
def UserOrdersList(request):
    permission_classes = [IsAuthenticated]
    user = request.user
    user_orders  = User_Order.objects.filter(user=user)
    serializer = UserUser_OrderSerializer(user_orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def UserOrdersDetail(request, pk):
    
    user_order = User_Order.objects.get(id=pk)
    serializer = UserUser_OrderSerializer(user_order, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def UserOrdersUpdate(request, pk):
    permission_classes = [IsAuthenticated]
    user_order = User_Order.objects.get(id=pk)
    if request.method == 'PUT':

        serializer = UserUser_OrderSerializer(instance=user_order, data=request.data, many = False, partial=True)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['GET'])
def ProfileView(request):
    permission_classes = [IsAuthenticated]
   # user = request.user.pk
    profile = Profile.objects.filter(user=request.user)
    serializer = UserProfileSerializer(profile, many=True)

    return Response(serializer.data)