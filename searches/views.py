from django.shortcuts import render

from blog.models import Post
from .models import SearchQuery

def search(request):
	query = request.GET.get('q', None)
	user = None

	if request.user.is_authenticated:
		user = request.user

	context = { 'query': query }

	if query is not None:
		SearchQuery.objects.create(user=user, query=query)
		posts = Post.objects.search(query=query)
		context['posts'] = posts

	return render(request, 'search.html', context)