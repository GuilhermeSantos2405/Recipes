from django.urls import path

from .views import IndexTemplateview, SearchTemplateview

urlpatterns = [
    path('', IndexTemplateview.as_view(), name='index'),
    path('search/', SearchTemplateview.as_view(), name='search'),
]
