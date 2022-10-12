from django import forms

from .models import Recipe


class RecipeRegisterView(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['title', 'preparation_time', 'servings',
                  'ingredients', 'preparation_method', 'image', 'category']
