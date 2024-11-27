from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.Book_View.as_view()),
    path('book/<int:pk>/', views.Book_Details.as_view()),
    path('book/isbn/<str:isbn>/', views.get_book_by_isbn),
    path('book/author/<str:author>/', views.get_book_by_author),
    path('book/genere/<str:genere>/', views.get_book_by_genere),
    path('book/copies/<str:var>/<int:count>/', views.get_book_by_copies_count),
    path('book/sort/<str:var>/', views.sort_books)
]