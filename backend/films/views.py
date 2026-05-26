from django.db.models import Count
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Category, Film
from .serializers import CategorySerializer, FilmSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.annotate(films_count=Count('films')).order_by('name')
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.select_related('category').all().order_by('-rating', 'title')
    serializer_class = FilmSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'director', 'country', 'category__name']
    ordering_fields = ['title', 'year', 'rating', 'duration']
