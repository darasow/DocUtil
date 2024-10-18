from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .forms import BookForm, ISBNForm
from .models import ISBN, Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre le livre en base de données
          # Redirige vers la liste des livres après ajout
            return redirect('books:book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books:book_list')

def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        # Liaison avec l'instance existante
        form = BookForm(request.POST, instance=book)  
        if form.is_valid():
            form.save()  # Met à jour l'auteur existant
            return redirect('books:book_list')
    else:
         # Pré-remplissage pour modification
        form = BookForm(instance=book) 
    return render(request, 'books/book_form.html', {'form': form})






def code_list(request):
    codes = ISBN.objects.all()
    return render(request, 'books/code_list.html', {'codes': codes})

def add_code(request):
    if request.method == 'POST':
        form = ISBNForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre le code ISBN
         # Redirige vers la liste des codes
            return redirect('books:code_list') 
    else:
        form = ISBNForm()
    return render(request, 'books/code_form.html', {'form': form})

def code_delete(request, id):
    code = get_object_or_404(ISBN, id=id)
    code.delete()
    return redirect('books:code_list')

def code_update(request, id):
    code = get_object_or_404(ISBN, id=id)
    if request.method == 'POST':
        # Liaison avec l'instance existante
        form = ISBNForm(request.POST, instance=code)  
        if form.is_valid():
            form.save()  # Met à jour l'auteur existant
            return redirect('books:code_list')
    else:
         # Pré-remplissage pour modification
        form = ISBNForm(instance=code) 
    return render(request, 'books/code_form.html', {'form': form})