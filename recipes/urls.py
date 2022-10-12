
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .api import (RecipeAPIv2Detail, RecipeAPIv2List, RecipeAPIv3ViewSet,
                  RecipeAPIv4ViewSet, recipe_api_detail, recipe_api_list)
from .views import (CategoryTemplateView, IndexTemplateview, RecipeCreateView,
                    RecipeDetailView, SearchTemplateview)

recipe_api_v4_router = SimpleRouter()  # Por padrão sempre tem / no final
recipe_api_v4_router.register(
    'recipes/api/v4', RecipeAPIv4ViewSet,
)

urlpatterns = [
    path('', IndexTemplateview.as_view(), name='index'),
    path('search/', SearchTemplateview.as_view(), name='search'),
    path('category/<int:category_id>',
         CategoryTemplateView.as_view(), name='category'),
    path('detail/<int:pk>', RecipeDetailView.as_view(), name='detail'),
    path('recipe_create', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipes/api/v1', recipe_api_list, name='recipes_api_v1'),
    path('recipes/api/v1/<int:pk>', recipe_api_detail,
         name='recipes_api_v1_detail'),
    path('recipes/api/v2', RecipeAPIv2List.as_view(), name='recipes_api_v2'),
    path('recipes/api/v2/<int:pk>',
         RecipeAPIv2Detail.as_view(), name='recipes_api_v2'),
    path('recipes/api/v3', RecipeAPIv3ViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='recipes_api_v3'),
    path('recipes/api/v3/<int:pk>',
         RecipeAPIv3ViewSet.as_view({
             'get': 'retrieve',
             'patch': 'partial_update',
             'delete': 'destroy',
         }), name='recipes_api_v3'),

    path('recipes/api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('recipes/api/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),

    path('recipes/api/token/verify/',
         TokenVerifyView.as_view(), name='token_verify'),

]
urlpatterns += recipe_api_v4_router.urls
