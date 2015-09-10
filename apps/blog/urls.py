from django.conf.urls import url, include

# from recipes.views import api
from blog.views import front

# apipatterns = [
#     url(
#         regex=r"ˆ$",
#         view=api.IngredientCreateReadView.as_view(),
#         name="ingredient_rest_api"
#     ),
#     url(
#         regex=r"ˆ(?P<b64id>[-\w]+)/(?P<slug>[-\w]+)$",
#         view=api.IngredientReadUpdateDeleteView.as_view(),
#         name="ingredient_rest_api"
#     )
# ]

frontpatterns = [
    url(
        regex=r"^$",
        view=front.index,
        name="index"
    ),
    # url(
    #     regex=r"(?P<b64id>[-\w]+)/(?P<slug>[-\w]+)",
    #     view=front.IngredientDetailView.as_view(),
    #     name="detail"
    # ),
]

urlpatterns = [
    url(
        r"^", include(frontpatterns, namespace="front")
    ),
    # url(
    #     r"^api/", include(apipatterns, namespace="api")
    # ),
]
