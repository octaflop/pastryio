from django.views.generic import ListView, DetailView

from recipes.models import Ingredient


class IngredientListView(ListView):
    template_name = "recipes/front/index.html"
    model = Ingredient


class IngredientDetailView(DetailView):
    model = Ingredient
