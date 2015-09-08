from django.conf.urls import url

from recipes import views

urlpatterns = [
    url(
        regex=r"ˆapi/$",
        view=views.IngredientCreateReadView.as_view(),
        name="ingredient_rest_api"
    ),
    url(
        regex=r"ˆapi/(?P<base36>[-\w]+)/$",
        view=views.IngredientReadUpdateDeleteView.as_view(),
        name="ingredient_rest_api"
    )
]
