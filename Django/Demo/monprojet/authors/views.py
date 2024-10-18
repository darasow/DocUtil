from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from .forms import AuthorForm
from .models import Author
from faker import Faker

# Initialiser Faker
fake = Faker()

# Afficher la liste des auteurs
def author_list(request):
    authors = Author.objects.all().order_by('-created_at')
    return render(request, 'authors/author_list.html', {'authors': authors})

# Détails d'un auteur
def author_detail(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, 'authors/author_detail.html', {'author': author})

# # Ajouter un auteur avec des données factices via Faker
# def add_author(request):
#     author = Author(
#         name=fake.name(),  # Générer un nom factice
#         birthdate=fake.date_of_birth(),  # Générer une date de naissance factice
#         biography=fake.text()  # Générer une biographie factice
#     )
#     author.save()
#     return HttpResponseRedirect('/authors/')
# def add_author(request):
#     if request.method == 'POST':
#         form = ClassicAuthorForm(request.POST)
#         if form.is_valid():
#             # Crée un objet Author à partir des données du formulaire
#             Author.objects.create(
#                 name=form.cleaned_data['name'],
#                 birthdate=form.cleaned_data['birthdate'],
#                 biography=form.cleaned_data.get('biography', '')
#             )
#             return redirect('authors:author_list')  # Redirige après l'ajout
#     else:
#         form = ClassicAuthorForm()
#     return render(request, 'authors/author_form.html', {'form': form})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre directement l'auteur en base de données
            return redirect('authors:author_list')
    else:
        form = AuthorForm()
    return render(request, 'authors/author_form.html', {'form': form})


# Supprimer un auteur
def delete_author(request, id):
    author = get_object_or_404(Author, id=id)
    author.delete()
    return HttpResponseRedirect('/authors/')

# Mettre à jour un auteur avec des données factices via Faker
# def update_author(request, id):
#     author = get_object_or_404(Author, id=id)
#     author.name = fake.name()  # Nouveau nom factice
#     author.birthdate = fake.date_of_birth()  # Nouvelle date de naissance factice
#     author.biography = fake.text()  # Nouvelle biographie factice
#     author.save()
#     return HttpResponseRedirect('/authors/')



# def update_author(request, id):
#     author = get_object_or_404(Author, id=id)
#     if request.method == 'POST':
#         form = ClassicAuthorForm(request.POST, initial={
#             'birthdate': author.birthdate,
#             'name': author.name,
#             'biography': author.biography
#         })
#         if form.is_valid():
#             author.name = form.cleaned_data['name']
#             author.birthdate = form.cleaned_data['birthdate']
#             author.biography = form.cleaned_data['biography']
#             author.save()
#             return redirect('authors:author_list')
#     else:
#         form = ClassicAuthorForm(initial={
#             'birthdate': author.birthdate,
#             'name': author.name,
#             'biography': author.biography
#         })  # Pré-remplissage pour modification
#     return render(request, 'authors/author_form.html', {'form': form})

def update_author(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        # Liaison avec l'instance existante
        form = AuthorForm(request.POST, instance=author)  
        if form.is_valid():
            form.save()  # Met à jour l'auteur existant
            return redirect('authors:author_list')
    else:
         # Pré-remplissage pour modification
        form = AuthorForm(instance=author) 
    return render(request, 'authors/author_form.html', {'form': form})