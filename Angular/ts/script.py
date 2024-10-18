from django.shortcuts import render, get_object_or_404
from .models import Publisher

def publisher_list(request):
    publishers = Publisher.objects.all() 
     # Récupère tous les éditeurs
    return render(request, 'publishers/publisher_list.html', {'publishers': publishers}) 
    # Rendu de la liste des éditeurs

def publisher_detail(request, id):
    publisher = get_object_or_404(Publisher, id=id) 
     # Récupère un éditeur par ID ou renvoie une 404
    return render(request, 'publishers/publisher_detail.html', {'publisher': publisher})  
    # Rendu des détails de l'éditeur