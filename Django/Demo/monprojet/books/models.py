from django.utils import timezone
from django.db import models
from authors.models import Author
from publishers.models import Publisher

class ISBN(models.Model):
    code = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(null=True, blank=True)
    modified_at = models.DateTimeField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Si l'objet est en train d'être créé
            self.created_at = timezone.now()
            self.modified_at = None
        else:
            self.modified_at = timezone.now()
        super(ISBN, self).save(*args, **kwargs)

    def __str__(self):
        return self.code

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    summary = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey (plusieurs livres peuvent avoir un même auteur)
    isbn = models.OneToOneField(ISBN, on_delete=models.CASCADE)  # OneToOneField (chaque livre a un ISBN unique)
    publishers = models.ManyToManyField(Publisher)  # ManyToManyField (un livre peut avoir plusieurs éditeurs)

    created_at = models.DateTimeField(null=True, blank=True)
    modified_at = models.DateTimeField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Si l'objet est en train d'être créé
            self.created_at = timezone.now()
            self.modified_at = None
        else:
            self.modified_at = timezone.now()
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
