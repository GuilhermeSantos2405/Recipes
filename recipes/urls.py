from django.urls import path

from .api import recipe_api_list
from .views import (CategoryTemplateView, IndexTemplateview, RecipeCreateView,
                    RecipeDetailView, SearchTemplateview)

urlpatterns = [
    path('', IndexTemplateview.as_view(), name='index'),
    path('search/', SearchTemplateview.as_view(), name='search'),
    path('category/<int:category_id>',
         CategoryTemplateView.as_view(), name='category'),
    path('detail/<int:pk>', RecipeDetailView.as_view(), name='detail'),
    path('recipe_create', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipes/api/v1', recipe_api_list, name='recipes_api_v1')
]
