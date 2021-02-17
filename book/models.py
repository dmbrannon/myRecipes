from django.db import models
from django.utils import timezone

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    source = models.CharField(max_length=200)
    steps = models.TextField()
    tries = models.IntegerField(default=0)
    icon = models.ForeignKey(
        'Icon',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.ManyToManyField(Recipe)

class MeasurementUnit(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.ManyToManyField(Recipe)

class MeasurementQty(models.Model):
    amount = models.CharField(max_length=50)
    recipe = models.ManyToManyField(Recipe)

class Note(models.Model):
    text = models.TextField()
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE
    )
    date_created = models.DateField(default=timezone.now)
    date_modified = models.DateField(auto_now=True)

class Icon(models.Model):
    code = models.CharField(max_length=10)

