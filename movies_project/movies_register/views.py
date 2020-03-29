from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .forms import  MovieForm


from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib import messages
import logging

from django.db import models
from django.db import connection

from .forms import DocumentForm
from .models import Movies

import csv, io
import codecs


# Create your views here.# one parameter named request
def movies_upload(request):    # declaring template
    template = "movies.html"
    data = Movies.objects.all()# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be title, actor ,writer ,genre  ,country ,director, rating ,score  ,year  ,release,runtime',
        'movies': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']    # let's check if it is a csv file

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Movies.objects.update_or_create(
            title = column[1],
            actor = column[2],
            writer = column[3],
            genre = column[4],
            country = column[5],
            director = column[6],
            rating = column[7],
            score = column[8],
            year = column[9],
            runtime =column[11],

            release = column[10]
        )
    context = {}
    return render(request, template, context)
# Create your views here.

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