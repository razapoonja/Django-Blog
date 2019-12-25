from django.conf import settings
from django.db import models
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class PostQuerySet(models.QuerySet):
	def published(self):
		now = timezone.now()
		return self.filter(publish_date__lte=now)

class PostManager(models.Manager):
	def get_queryset(self):
		return PostQuerySet(self.model, using=self._db)

	def published(self):
		return self.get_queryset().published()

class Post(models.Model):
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	image = models.ImageField(upload_to='image/', null=True, blank=True)
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	content = models.TextField(null=True, blank=True)
	publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	objects = PostManager()

	class Meta:
		ordering = ['-publish_date', '-updated', '-timestamp']

	def get_absolute_url(self):
		return f"/blog/{self.slug}"

	def get_edit_url(self):
		return f"{self.get_absolute_url()}/edit"

	def get_delete_url(self):
		return f"{self.get_absolute_url()}/delete"