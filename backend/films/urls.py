from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, FilmViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'films', FilmViewSet, basename='film')

urlpatterns = [
    path('', include(router.urls)),
]
