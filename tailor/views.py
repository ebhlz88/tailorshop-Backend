from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import status


from .models import customer,order
from .Serializers import customerSerializer,orderSerializer
from rest_framework.views import APIView

# Create your views here.
class customersearch(ListAPIView):
        queryset=customer.objects.all()
        serializer_class=customerSerializer
        filter_backends=[SearchFilter]
        search_fields=['name','fm_number','id']

class ordersearch(ListAPIView):
        queryset=customer.objects.all()
        serializer_class=orderSerializer
        filter_backends=[SearchFilter]
        search_fields=['name','fm_number']


class customerclass(APIView):
    def get(self,request,format=None):
        allcustomers = customer.objects.all()
        serialized_customer = customerSerializer(allcustomers,many=True)
        return Response(serialized_customer.data, status=status.HTTP_201_CREATED)
    def post(self,request,format=None):
        serialized_customer = customerSerializer(request.data)
        if serialized_customer.is_valid():
            serialized_customer.save()
            return Response(serialized_customer.data, status=status.HTTP_201_CREATED)
        return Response(serialized_customer.errors, status=status.HTTP_400_BAD_REQUEST)

class orderupdate(APIView):
    def get(self,request,pkk,format=None):
        allcustomers = order.objects.filter(pk=pkk)
        serialized_order = orderSerializer(allcustomers,many=True)
        return Response(serialized_order.data, status=status.HTTP_201_CREATED)
    def post(self,request,pkk,format=None):
        orderr = order.objects.get(pk=pkk)
        serialized_order = orderSerializer(orderr, request.data,partial=True)
        if serialized_order.is_valid():
            serialized_order.save()
            return Response(serialized_order.data, status=status.HTTP_201_CREATED)
        return Response(serialized_order.errors, status=status.HTTP_400_BAD_REQUEST)

class orderclass(APIView):
    def get(self,request,pk,format=None):
        allcustomers = order.objects.filter(customerFK__id=pk)
        serialized_order = orderSerializer(allcustomers,many=True)
        return Response(serialized_order.data, status=status.HTTP_201_CREATED)

class orderpost(APIView):
    def post(self,request,format=None):
        serialized_order = orderSerializer(data=request.data)
        if serialized_order.is_valid():
            serialized_order.save()
            return Response(serialized_order.data, status=status.HTTP_201_CREATED)
        return Response(serialized_order.errors, status=status.HTTP_400_BAD_REQUEST)
