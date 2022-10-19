from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import Http404
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from api.serializers import ShippingSerializer, ImageSerializer, CommentSerializer, \
    CategorySerializer, ProductSerializer
from api.serializers.serializers import *
from api.models import Category, Product, Shipping, Comment, Image


class CategoryListAPIView1(APIView):
    def get(self,request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ProductListAPIView1(APIView):
    def get(self,request):
        Products = Product.objects.all()
        serializer = CategorySerializer(Products, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



