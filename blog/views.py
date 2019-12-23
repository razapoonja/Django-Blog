# from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import PostForm

def post_list(request):
	posts = Post.objects.all()
	context = {'posts': posts}

	return render(request, 'post/list.html', context)

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	context = {'post': post}

	return render(request, 'post/detail.html', context)

@staff_member_required
def post_create(request):
	form = PostForm(request.POST or None)

	if form.is_valid():
		post = form.save()
		form = PostForm()

	context = {'form': form}

	return render(request, 'form.html', context)

def post_update(request, slug):
	post = get_object_or_404(Post, slug=slug)
	context = {'post': post}

	return render(request, 'post/update.html', context)

def post_delete(request, slug):
	return
