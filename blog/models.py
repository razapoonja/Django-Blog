from django.db import models

class Post(models.Model):
	title = models.TextField()
	slug = models.SlugField(unique=True)
	content = models.TextField(null=True, blank=True)