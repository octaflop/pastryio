from django.conf.urls import url, include

from profiles.views.front import detail, index

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
    # url(
    #     regex=r"ˆapi/$",
    #     view=views.IngredientCreateReadView.as_view(),
    #     name="ingredient_rest_api"
    # ),
    # url(
    #     regex=r"ˆapi/(?P<base36>[-\w]+)/$",
    #     view=views.IngredientReadUpdateDeleteView.as_view(),
    #     name="ingredient_rest_api"
    # )
]

urlpatterns = [
    url(
        r"^", include(frontpatterns, namespace="front")
    ),
]
