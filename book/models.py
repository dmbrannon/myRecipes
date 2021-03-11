from django.db import models
from django.utils import timezone

class Ingredient(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=128)
    source = models.CharField(max_length=256)
    sourceName = models.CharField(max_length=64, default='Dana')
    steps = models.TextField()
    tries = models.IntegerField(default=0)
    icon = models.ForeignKey(
        'Icon',
        on_delete=models.CASCADE,
    )
    ingredients = models.ManyToManyField(Ingredient, through='Measurement')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Measurement(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    qty = models.CharField(max_length=64)
    unit = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.qty} {self.unit} {self.ingredient}"

class Note(models.Model):
    text = models.TextField()
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE
    )
    date_created = models.DateField(default=timezone.now)
    date_modified = models.DateField(auto_now=True)

class Icon(models.Model):
    code = models.CharField(max_length=8)

