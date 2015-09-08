from django.conf.urls import url, include

from recipes.views import api
from recipes.views import front

apipatterns = [
    url(
        regex=r"ˆ$",
        view=api.IngredientCreateReadView.as_view(),
        name="ingredient_rest_api"
    ),
    url(
        regex=r"ˆ(?P<base36>[-\w]+)/$",
        view=api.IngredientReadUpdateDeleteView.as_view(),
        name="ingredient_rest_api"
    )
]

frontpatterns = [
    url(
        regex=r"^$",
        view=front.IngredientListView.as_view(),
        name="index"
    ),
    # url(
    #     regex=r"^(?P<b36id>\w+)$",
    #     view=detail,
    #     name="detail"
    # ),
]

urlpatterns = [
    url(
        r"^", include(frontpatterns, namespace="front")
    ),
    url(
        r"^api/", include(apipatterns, namespace="api")
    ),
]
