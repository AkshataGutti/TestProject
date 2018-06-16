
# Create your views here.
from django.shortcuts import render
from .models import Board
from .forms import PostForm
from django.db.models import Q
from django.contrib import messages
from django.http.response import HttpResponseRedirect

def home(request):
    form = PostForm(request.POST)
    if request.method == "POST": 
        if form.is_valid():
            form.save()
    return render(request, 'homepage.html',{'form':form})
def details(request):
    user = Board.objects.all().count()
    return render(request, 'index.html', {'user':user})
def User(request):
    user = Board.objects.all().count()
    lists = Board.objects.all()
    return render(request, 'base.html',{'user': user,'lists': lists})

def Search(request): 
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:
            match = Board.objects.filter(Q(name__icontains=srch))
            if match:
                return render(request, 'search.html',{'sr': match})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request, 'search.html')

def login(request):
    return render(request, 'login.html')