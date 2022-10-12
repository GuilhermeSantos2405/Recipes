from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .forms import RecipeRegisterView
from .models import Recipe


class ListBaseView(ListView):
    context_object_name = 'recipes_list'
    model = Recipe
    paginate_by = '6'


class IndexTemplateview(ListBaseView):
    template_name = 'pages/index.html'

    def get_queryset(self):
        return Recipe.objects.filter(is_published=True).order_by('?')


class CategoryTemplateView(ListBaseView):
    template_name = 'pages/category.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(category__id=self.kwargs.get(
            'category_id'), is_published=True)
        return qs


class SearchTemplateview(ListBaseView):
    template_name = 'pages/search.html'

    def get_queryset(self):
        search_term = self.request.GET.get('search_term')
        qs = Recipe.objects.filter(
            title__icontains=search_term, is_published=True)
        return qs


class RecipeDetailView(DetailView):
    template_name = 'pages/detail.html'
    login_url = reverse_lazy('login')
    model = Recipe

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(is_published=True)
        return qs


class RecipeCreateView(LRM, CreateView):
    login_url = reverse_lazy('login')
    model = Recipe
    template_name = 'pages/create_recipe.html'
    form_class = RecipeRegisterView
    success_url = reverse_lazy('index')

    def form_valid(self, form=RecipeRegisterView):
        form.instance.author = self.request.user
        url = super().form_valid(form)
        return url
