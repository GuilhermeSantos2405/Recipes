from django.views.generic import TemplateView


class IndexTemplateview(TemplateView):
    template_name = 'pages/index.html'


class SearchTemplateview(TemplateView):
    template_name = 'pages/search.html'
