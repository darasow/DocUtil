from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    # Liste des auteurs
    path('', views.author_list, name='author_list'),  
      # Détails d'un auteur
    path('<int:id>/', views.author_detail, name='author_detail'), 
      # Ajouter un auteur
    path('add_author/', views.add_author, name='add_author'), 
      # Supprimer un auteur
    path('delete_author/<int:id>/', views.delete_author, name='delete_author'), 
    # Mettre à jour un auteur
    path('update_author/<int:id>/', views.update_author, name='update_author'),  
]
