from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    biography = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True)
    modified_at = models.DateTimeField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Si l'objet est en train d'être créé
            self.created_at = timezone.now()
            self.modified_at = None
        else:
            self.modified_at = timezone.now()
        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
