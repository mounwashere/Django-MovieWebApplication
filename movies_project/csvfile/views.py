import csv, io
import datetime
import pandas as pd
import codecs
from django.shortcuts import render
from django.contrib import messages
from .models import Profile
from movies_register.models import Movies
# Create your views here.# one parameter named request


def profile_upload(request):    # declaring template
    template = "profile_upload.html"
    data = Movies.objects.all()
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be title, actor ,writer ,genre  ,country ,director, rating ,score  ,year  ,release,runtime',
        'movies': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']


        # CVS handling here.

    # let's check if it is a csv file

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



    '''
    for row in csv.reader(io_string, delimiter=',', quotechar="|"):
       print(repr(datetime.datetime.strptime(row[9], display_format).strftime(db_format)))
       some = row[1]
    mymodels = Movies.objects.all()
    len(mymodels)
    '''

    '''
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _,  created = Movies.objects.update_or_create(
            title = column[0],
            actor = column[1],
            writer = column[2],
            genre = column[3],
            country = column[4],
            director = column[5],
            rating = column[6],
            score = column[7],
            year = column[8],
            release = datetime.datetime.strptime(column[9], display_format).strftime(db_format),
            runtime =column[10]
        )

    '''

    # reader = csv.DictReader(codecs.iterdecode(f, 'utf-8'))
    context = {}
    return render(request, template, context)






