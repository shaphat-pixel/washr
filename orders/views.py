from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
from rest_framework.decorators import api_view
from uritemplate import partial
from .serializers import *
from . models import *
# Create your views here.


@login_required
@api_view(['GET'])
def OrdersList(request):
    permission_classes = [IsAuthenticated]
    orders = Orders.objects.all()
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def OrdersDetail(request, pk):
    orders = Orders.objects.get(id=pk)
    serializer = OrdersSerializer(orders, many=False)
    return Response(serializer.data)

@login_required
@api_view(['POST'])
def OrdersCreate(request):
    if request.method == "POST":

        serializer = OrdersSerializer(data=request.data)
        
    if serializer.is_valid():
            
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def OrdersUpdate(request, pk):
    orders = Orders.objects.get(id=pk)
    serializer = OrdersSerializer(instance=orders, data=request.data, many=False, partial="True")

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def OrdersDelete(request, pk):
    orders = Orders.objects.get(id=pk)
    orders.delete()

    return Response('order successfully deleted')