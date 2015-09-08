from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from pastryio.models.mixins import ArchiveMixin
from profiles.models import BaseProfile


class Ingredient(ArchiveMixin):
    name = models.CharField(_("Name"), max_length=254)
    calories = models.IntegerField(_("Calories"), blank=True, default=0)

    @property
    def slug(self):
        return slugify(self.name)


class Recipe(ArchiveMixin):
    title = models.CharField(_("Title"), max_length=254)
    author = models.ForeignKey(BaseProfile)
    ingredients = models.ManyToManyField(Ingredient)
    photo = models.ImageField(_("Photo"), blank=True)

    @property
    def slug(self):
        return slugify(self.title)

    # def get_absolute_url(self):
        # return reverse("")


class RecipeStep(ArchiveMixin):
    step = models.PositiveIntegerField(_("Step"))
    description = models.TextField(_("Description"))
    recipe = models.ForeignKey(Recipe)
    photo = models.ImageField(_("Photo"), blank=True)
