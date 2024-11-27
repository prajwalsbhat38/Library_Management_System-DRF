from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Books
from .serializer import Books_Serializer

# Create your views here.
class Book_View(APIView):
    def get(self, request):
        data = Books.objects.all()
        serializer = Books_Serializer(data, many = True, context = {'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = Books_Serializer(data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Book_Details(APIView):
    def get(self, request, pk):
        try:
            data = Books.objects.get(pk = pk)
            serializer = Books_Serializer(data, context = {'request': request})
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Books.DoesNotExist:
            return Response({'error': f'Book with ID: {pk} not found'})
    
    def put(self, request, pk):
        try:
            data = Books.objects.get(pk = pk)
            serializer = Books_Serializer(data, data = request.data, context = {'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Books.DoesNotExist:
            return Response({'error': f'Book with ID: {pk} not found'})
    
    def delete(self, request, pk):
        try:
            data = Books.objects.get(pk = pk)
            data.delete()
            return Response({'response': f'Book with ID: {pk} deleted'}, status=status.HTTP_202_ACCEPTED)
        except Books.DoesNotExist:
            return Response({'error': f'Book with ID: {pk} not found'})

@api_view(['GET',])
def get_book_by_isbn(request, isbn):
    try:
        data = Books.objects.get(isbn = isbn)
        serializer = Books_Serializer(data, context = {'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Books.DoesNotExist:
        return Response({'error': f'Book with ISBN: {isbn} not found'})

@api_view(['GET',])
def get_book_by_author(request, author):
    data = Books.objects.filter(author = author)
    if data.exists():
        serializer = Books_Serializer(data, many = True, context = {'request': request})
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response({'response': f'Books with author name: {author} doesnot exist'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET',])
def get_book_by_genere(request, genere):
    data = Books.objects.filter(genere = genere)
    if data.exists():
        serializer = Books_Serializer(data, many = True, context = {'request': request})
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response({'response': f'Book with genere: {genere} not found'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET',])
def get_book_by_copies_count(request, var, count):
    if count<1:
        return Response({'error': 'Count cannot be less than 0'}, status=status.HTTP_400_BAD_REQUEST)
    data = Books
    if var == 'lt':
        data = Books.objects.filter(copies__lt=count)
    elif var == 'gt':
        data = Books.objects.filter(copies__gt=count)
    else:
        return Response({'error': 'Please provie lt: for less than operation and gt for greater than operation'})
    if data.exists():
        serializer = Books_Serializer(data, many = True, context = {'request': request})
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response({'error': 'No Books found'})

@api_view(['GET',])
def sort_books(request, var):
    if var in ['title', 'author', 'isbn', 'genere', 'copies']:
        data = Books.objects.all().order_by(var)
        serializer = Books_Serializer(data, many = True, context = {'request': request})
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response({'error': 'Invalid Variable -> allowed variables are [title, author, isbn, genere, copies]'})