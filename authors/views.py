
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, UpdateView
from django.views.generic.edit import CreateView
from recipes.models import Recipe

from .forms import Registerform


class AuthorRecipesView(ListView):
    template_name = 'pages/authors_recipes_views.html'
    context_object_name = 'authors_recipes'
    model = Recipe
    paginate_by = 6

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(author_id=self.kwargs.get(
            'author_id'), is_published=True)
        return qs


class AuthorsCreateView(CreateView):
    template_name = 'pages/create_authors.html'
    form_class = Registerform
    success_url = reverse_lazy('login')


class AuthorsDeleteView(DeleteView):
    model = Recipe
    template_name = 'pages/delete_recipe.html'
    success_url = reverse_lazy('index')


class AuthorsUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'preparation_time', 'servings', 'is_published',
              'ingredients', 'preparation_method', 'image', 'category']
    template_name = 'pages/update_recipe.html'
    success_url = reverse_lazy('index')
