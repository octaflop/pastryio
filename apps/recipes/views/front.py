from django.views.generic import ListView, DetailView

from recipes.models import Ingredient


class IngredientListView(ListView):
    template_name = "recipes/front/index.html"
    model = Ingredient
    context_object_name = "ingredients"


class IngredientDetailView(DetailView):
    model = Ingredient
