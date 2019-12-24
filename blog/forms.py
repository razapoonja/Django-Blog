from django import forms

from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'slug', 'content']

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get('title')
		post = Post.objects.filter(title__iexact=title)

		instance = self.instance
		if instance is not None:
			post = post.exclude(pk=instance.pk)

		if post.exists():
			raise forms.ValidationError('This title has already been used. Please try again.')

		return title