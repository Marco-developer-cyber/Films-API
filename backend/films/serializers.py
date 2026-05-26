from rest_framework import serializers

from .models import Category, Film


class CategorySerializer(serializers.ModelSerializer):
    films_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'films_count']


class FilmSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source='category',
        queryset=Category.objects.all(),
        write_only=True
    )
    rating = serializers.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        model = Film
        fields = [
            'id',
            'category',
            'title',
            'year',
            'director',
            'rating',
            'duration',
            'country',
            'poster_url',
            'description',
            'highlight',
            'category_id',
        ]
