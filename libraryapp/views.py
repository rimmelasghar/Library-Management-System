from django.shortcuts import render
from .models import Book
# Create your views here.

def Home(request):
    books = Book.objects.all()
    count = Book.objects.count()
    return render(request,'home.html',{'books':books,'count':count})