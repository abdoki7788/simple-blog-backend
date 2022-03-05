from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=300)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def get_date(self):
		return f"{self.updated.year}-{self.updated.month}-{self.updated.day}"

	def __str__(self):
		return self.title