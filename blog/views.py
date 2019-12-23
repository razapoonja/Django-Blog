from django.shortcuts import render, get_object_or_404, redirect

from .models import Post

def post_list(request):
	posts = Post.objects.all()
	context = {'posts': posts}

	return render(request, 'post_list.html', context)

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	context = {'post': post}

	return render(request, 'post_detail.html', context)

def post_create(request):
	context = {'form': None}

	return render(request, 'post_create.html', context)

def post_update(request, slug):
	post = get_object_or_404(Post, slug=slug)
	context = {'post': post}

	return render(request, 'post_update.html', context)

def post_delete(request, slug):
	return
