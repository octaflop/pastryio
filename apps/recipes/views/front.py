from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from recipes.models import Ingredient


class IngredientListView(ListView):
    template_name = "recipes/front/index.html"
    model = Ingredient
    context_object_name = "ingredients"


class IngredientDetailView(DetailView):
    template_name = "recipes/front/detail.html"
    model = Ingredient
    context_object_name = "ingredient"

    def get_object(self):
        return get_object_or_404(Ingredient, b64id=self.kwargs['b64id'])
