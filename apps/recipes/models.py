from django.db import models
from pastryio.models.mixins import ArchiveMixin


class Ingredient(ArchiveMixin):
    name = models.CharField(max_length=254)
    calories = models.IntegerField(blank=True)


class Recipe(ArchiveMixin):
    title = models.CharField(max_length=254)


class RecipeStep(ArchiveMixin):
    step = models.PositiveIntegerField()
    description = models.TextField()
    recipe = models.ForeignKey(Recipe)
