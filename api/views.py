from rest_framework.viewsets import ModelViewSet
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.


class ArticleViewSet(ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	lookup_field = 'slug'