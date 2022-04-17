from itsdangerous import Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Book
from .serializers import BookSerializer
from django.http import JsonResponse
from django.shortcuts import render

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/book-list/',
        'Detail View': '/book-detail/<str:pk>/',
        'Create': '/book-create/',
        'Update': '/book-update/<str:pk>/',
        'Delete': '/book-delete/<str:pk>/',
         }   
    return Response(api_urls)

@api_view(['GET'])
def bookList(request):
    books = Book.objects.all()    
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bookDetail(request, pk):
    books = Book.objects.get(id=pk)    
    serializer = BookSerializer(books, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def bookCreate(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def bookUpdate(request,pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def bookDelete(request,pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return Response(serializer.data)