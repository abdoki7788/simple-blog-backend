from rest_framework import serializers
from .models import Article
from django.contrib.auth import get_user_model

User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = ['title', 'slug', 'content']


class CurrentUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', 'id', 'first_name', 'last_name', 'get_full_name')