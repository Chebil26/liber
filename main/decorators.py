from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return render(request, 'home.html', {})
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func