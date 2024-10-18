from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    # Les route pour les livres
    path('', views.book_list, name='book_list'),
    path('<int:id>/', views.book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('update_book/<int:id>/', views.update_book, name='update_book'),
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
    # Les route pour les codes
    path('codes/', views.code_list, name='code_list'),
    path('add_code/', views.add_code, name='add_code'),
    path('code_delete/<int:id>', views.code_delete, name='code_delete'),
    path('code_update/<int:id>', views.code_update, name='code_update'),
]
