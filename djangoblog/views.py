from django.shortcuts import render

from .forms import Contact

def contact(request):
	form = Contact(request.POST or None)

	if form.is_valid():
		form = Contact()

	return render(request, 'form.html', {'form': form})
