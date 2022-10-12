
from rest_framework import serializers

from .models import Category, Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'preparation_time', 'preparation_choices',
            'servings_choices', 'ingredients', 'preparation_method',
            'is_published', 'category',
        ]

        is_published = serializers.BooleanField(
            source='Public',
            read_only=True,)  # Não vai aceitar dados de retorno da API

        # juntando campos do models
        servings = serializers.SerializerMethodField()

        def get_servings(self, recipe):
            return f'{ recipe.servings} {recipe.servings_choices}'

        category = serializers.PrimaryKeyRelatedField(
            queryset=Category.objects.all(),)

        category_name = serializers.StringRelatedField(
            source='category'
        )

        author = serializers.StringRelatedField(
        )


""" class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=65)
    preparation_choices = serializers.CharField(max_length=65)
    # Utilizando nome diferente do models
    methods = serializers.CharField(source='preparation_method')

    # juntando campos do models
    servings = serializers.SerializerMethodField()

    def get_servings(self, recipe):
        return f'{ recipe.servings} {recipe.servings_choices}'

    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
    )

    category_name = serializers.StringRelatedField(
        source='category'
    )

    author = serializers.StringRelatedField(
    )

    is_published = serializers.BooleanField(
        read_only=True,  # Somente leitura
    ) """
