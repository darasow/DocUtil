from django import forms
import datetime
# class ClassicAuthorForm(forms.Form):
#     name = forms.CharField(max_length=100, label="Nom de l'auteur")
#     birthdate = forms.DateField(widget=forms.SelectDateWidget( years=range(1800, datetime.date.today().year + 1)),
#                                  label="Date de naissance")
#     biography = forms.CharField(widget=forms.Textarea, label="Biographie", required=False)
    
#     def __init__(self, *args, **kwargs):
#         # Si des données initiales sont fournies, les utiliser pour remplir le formulaire
#         initial = kwargs.get('initial', {})
#         super(ClassicAuthorForm, self).__init__(*args, **kwargs)
#         if initial:
#             self.fields['birthdate'].initial = initial.get('birthdate')
#             self.fields['name'].initial = initial.get('name')
#             self.fields['biography'].initial = initial.get('biography')



from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Date de naissance"
    )
    class Meta:
        model = Author
        fields = ['name', 'birthdate', 'biography']

