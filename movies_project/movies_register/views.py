import datetime
from django.shortcuts import render, redirect
from .forms import  MovieForm
from django.shortcuts import render
from django.contrib import messages
from django.db.models import Count, Avg
from .models import Movies

import csv, io
import codecs



def profile_upload(request):    # declaring template
    data = Movies.objects.all()
    context = {'movies_list': Movies.objects.all()}
    template ="movies.html"
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be title, actor ,writer ,genre  ,country ,director, rating ,score  ,year  ,release,runtime',
        'movies': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, context)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    data_set = csv_file.read().decode('latin-1')

    display_format = '%m-%d-%Y'
    db_format = '%Y-%m-%d'
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    reader = csv.DictReader(codecs.iterdecode(csv_file, 'latin-1'))

    for row in reader:
        title = row['title']
        actor = row['actor']
        writer = row['writer']
        genre = row['genre']
        country = row['country']
        director = row['director']
        rating = row['rating']
        score = row['score']
        year = row['year']
        release = datetime.datetime.strptime(row['release'], display_format).strftime(db_format)
        runtime = row['runtime']
        Model = Movies(title=title, actor=actor, writer=writer, genre=genre, country=country,
                        director=director, rating=rating, score=score, year=year, release=release, runtime=runtime)
        try:
            Model.save()
        except Exception as e:
            messages.error(request, "Unable to save csv data to the database. " + repr(e))

    # reader = csv.DictReader(codecs.iterdecode(f, 'utf-8'))

    return render(request, template, context)


# Create your views here.

# Create your views here.
def home(request):
    return render(request, 'index.html')

def movies(request):
    return render(request, 'movies.html')

def charts(request):
    labels = ['Action','Adventure','Animation', 'Biography', 'Comedy','Crime', 'Drama', 'Family', 'Musical','Mystery', 'Romance', 'Science-Fiction','War','Western']
    data =  [1330, 390 , 277, 357, 2060, 517, 1429, 14, 31, 5, 37, 14, 13, 18, 1, 2]
    data2= [5.689818181818182, 6.108496240601504, 6.7143456962911126, 6.253846153846154, 6.351351351351352, 6.161019417475728, 5.877777777777777, 6.757640232108317, 6.4799999999999995, 5.787096774193548, 5.792857142857143, 7.041456582633054, 6.348461538461539, 6.057142857142857, 6.2, 6.746931407942238, 7.4]

   # labels.append(Movies.objects.values_list('genre', flat=True).order_by('genre').distinct())
   # print(labels)
    fieldname = 'genre'
    #dat = Movies.objects.values_list(fieldname).order_by(fieldname).annotate(the_count=Count(fieldname))
   # print(dat)
   # data.append(dat.values_list('the_count', flat=True).order_by('genre'))
    #print(data)
    '''
    
    dat2 = Movies.objects.values('genre').annotate(the_avg=Avg('score'))
    print(dat2)
    data2.append(dat2.values_list('the_avg', flat=True).order_by('genre'))
    print(data2)
    
    '''


    return render(request, 'charts.html', {
        'labels': labels,
        'data': data
    })

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


