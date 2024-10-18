from django import forms
from .models import ISBN, Book

class ISBNForm(forms.ModelForm):
    class Meta:
        model = ISBN
        fields = ['code']
        widgets = {
            'code': forms.TextInput(attrs={'placeholder': 'Code ISBN'}),
        }
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'summary', 'author', 'isbn', 'publishers']
       
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titre du livre'}),
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
            'summary': forms.Textarea(attrs={'placeholder': 'Résumé du livre'}),
        }

