
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Recipe
from .serializer import RecipeSerializer


class RecipeAPIv4ViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    # Sobre escrevendo métodos
    """ def get_serializer_class(self):
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["example"] = 'this is in context now'
        return context """


class RecipeAPIv3ViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        category_id = self.request.query_params.get('category_id', '')

        if category_id != '' and category_id.isnumeric():
            qs = qs.filter(category_id=category_id)

        return qs


class RecipeAPIv2List(ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeAPIv2Detail(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


@api_view()
def recipe_api_list(request):
    # Pegando todos os elementos
    recipes = Recipe.objects.get_queryset().filter(is_published=True)

    # Serializando (transformar em JSON) #many = True é pq está mandando vários elementos
    serializer = RecipeSerializer(instance=recipes, many=True)
    return Response(serializer.data)  # Retornando os dados


@api_view()
def recipe_api_detail(request, pk):
    recipe = get_object_or_404(
        Recipe.objects.filter(pk=pk, is_published=True)  # Pegando um elemento
    )
    # Serializando (transformar em JSON) #many = false é um
    serializer = RecipeSerializer(instance=recipe, many=False)
    return Response(serializer.data)  # Retornando os dados
