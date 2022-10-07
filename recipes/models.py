from django.contrib.auth.models import User
from django.db import models
from stdimage import StdImageField


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Base):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(Base):
    preparation_choices = [
        ('Minutos', 'Minutos'),
        ('Hora(s)', 'Hora(s)'),
    ]
    servings_choices = [
        ('Unidade(s)', 'Unidade(s)'),
        ('Porções', 'Porções'),
        ('Pessoa(s)', 'Pessoa(s)'),
    ]
    title = models.CharField(max_length=65)
    preparation_time = models.IntegerField()
    preparation_choices = models.CharField(
        max_length=12, choices=preparation_choices, default='')
    servings = models.IntegerField()
    servings_choices = models.CharField(
        max_length=12, choices=servings_choices, default='')
    ingredients = models.TextField()
    preparation_method = models.TextField()
    is_published = models.BooleanField(default=False, blank=True)
    image = StdImageField(upload_to='path/to/img',
                          variations={'variation_image':
                                      {'width': 370, 'height': 217}})

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Recipe')
        verbose_name_plural = ('Recipes')
