from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    director = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    country = models.CharField(max_length=100)
    poster_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    highlight = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, related_name='films', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
