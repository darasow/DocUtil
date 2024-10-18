from django.shortcuts import redirect, render, get_object_or_404

from .forms import PublisherForm
from .models import Publisher

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publishers/publisher_list.html', {'publishers': publishers})

def publisher_detail(request, id):
    publisher = get_object_or_404(Publisher, id=id)
    return render(request, 'publishers/publisher_detail.html', {'publisher': publisher})

def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre le livre en base de données
          # Redirige vers la liste des publishers après ajout
            return redirect('publishers:publisher_list')
    else:
        form = PublisherForm()
    return render(request, 'publishers/publisher_form.html', {'form': form})

def delete_publisher(request, id):
    publisher = get_object_or_404(Publisher, id=id)
    publisher.delete()
    return redirect('publishers:publisher_list')

def update_publisher(request, id):
    publisher = get_object_or_404(Publisher, id=id)
    if request.method == 'POST':
        # Liaison avec l'instance existante
        form = PublisherForm(request.POST, instance=publisher)  
        if form.is_valid():
            form.save()  # Met à jour l'edition existante
            return redirect('publishers:publisher_list')
    else:
         # Pré-remplissage pour modification
        form = PublisherForm(instance=publisher) 
    return render(request, 'publishers/publisher_form.html', {'form': form})
