 
from django.contrib.auth.forms import AuthenticationForm 
from urllib import request
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.urls import reverse
from django.shortcuts import render ,  redirect , get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q 



from main.forms import *
from .models import *
from .decorators import *


def home(request):
    queryset = Annonce.objects.all()
    print(queryset)
    context = {'annonce':queryset}
    return render(request, 'home.html', context)
    

def t(request):
    b = Book.objects.all()
    return render(request , 't.html',{'book':b} )


def annoce_search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        lookups = Q(book__title__icontains=searched) | Q(book__author__icontains=searched)
        annonce = Annonce.objects.filter(lookups)
        return render(request, 
		"annonce_search.html", 
		{'searched':searched,
		'annonce':annonce
        })
    else:
        return render(request, 
		"annonce_search.html", 
		{})
		
    

class annonce_detail(DetailView):
    queryset = Annonce.objects.all()
    template_name = "annonce_detail.html"

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(Annonce, id=id_)
 
 
#@login_required(login_url='login')    
class annonce_create(CreateView):

    queryset = Annonce.objects.all()
    form_class = AnnonceForm
    template_name="annonce_create.html"

    def form_valid(self, form) :
        obj = form.save(commit=False)
        obj.publisher = self.request.user    
        obj.save() 
        print(form.cleaned_data)
        return super().form_valid(form)
    
class annonce_list(ListView):

    queryset = Annonce.objects.all()
    template_name="home.html"
    

