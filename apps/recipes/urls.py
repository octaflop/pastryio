from django.conf.urls import url, include

from recipes.views.api import IngredientCreateReadView, IngredientReadUpdateDeleteView
from recipes.views.front import index, detail

apipatterns = [
    url(
        regex=r"ˆ$",
        view=IngredientCreateReadView.as_view(),
        name="ingredient_rest_api"
    ),
    url(
        regex=r"ˆ(?P<base36>[-\w]+)/$",
        view=IngredientReadUpdateDeleteView.as_view(),
        name="ingredient_rest_api"
    )
]

frontpatterns = [
    url(
        regex=r"^$",
        view=index,
        name="index"
    ),
    url(
        regex=r"^(?P<b36id>\w+)$",
        view=detail,
        name="detail"
    ),
]

urlpatterns = [
    url(
        r"^", include(apipatterns, namespace="api")
    ),
    url(
        r"^api/", include(frontpatterns, namespace="front")
    ),
]
