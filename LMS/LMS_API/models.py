from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=25)
    isbn = models.CharField(max_length=14, unique=True)
    genere = models.CharField(max_length=15)
    copies = models.IntegerField()

    def __str__(self):
        return self.title
