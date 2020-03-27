from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import  MovieForm
from .models import  Movies

# Create your views here.

def home(request):
    return render(request, 'index.html')

def movies(request):
    return render(request, 'movies.html')

def charts(request):
    return render(request, 'charts.html')


def movies_list(request):
    context = {'movies_list': Movies.objects.all()}
    return render(request, "movies.html", context)



def movies_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = MovieForm()
        else:
            movies = Movies.objects.get(pk=id)
            form = MovieForm(instance=movies)
        return render(request, "movies_form.html", {'form': form})
    else:
        if id == 0:
            form = MovieForm(request.POST)
        else:
            movies = Movies.objects.get(pk=id)
            form = MovieForm(request.POST,instance= movies)
        if form.is_valid():
            form.save()
        return redirect('/movies/list')


def movies_delete(request,id):
    movies = Movies.objects.get(pk=id)
    movies.delete()
    return redirect('/movies/list')

def about(request):
    return render(request, 'about.html', {'title': 'About'})
