from django.contrib import admin

from pastryio.admin.mixins import ArchiveAdminMixin
from recipes.models import Recipe, Ingredient

admin.site.register(Recipe, ArchiveAdminMixin)
admin.site.register(Ingredient, ArchiveAdminMixin)
