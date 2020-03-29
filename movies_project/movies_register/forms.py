import numpy
from django import forms
from .models import  Movies
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from movies_project import settings
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import widgets

from .models import Document


filetypes = [('csv', 'csv'),
             ]

separators = [('comma', 'comma'),
              ('tab', 'tab'),
              ]

SCORE = (
    [(i, i) for i in numpy.arange(0, 0.1, 10)]
)

class DocumentForm(forms.ModelForm):
    fileFormat = forms.CharField(label='File format:', widget=forms.Select(choices=filetypes))
    separator = forms.ChoiceField(label='Separator:', choices=separators, required=False, widget=forms.RadioSelect())

    class Meta:
        model = Document
        fields = ('fileFormat', 'document',)

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movies
        fields = ('title', 'actor','director', 'writer', 'genre' , 'country', 'rating', 'score','year','release',  'runtime')
        country = CountryField().formfield()
        score = forms.ChoiceField(label='Score:',choices=SCORE, required=False )
        #release1 = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, label='What is the date of release?', widget=forms.SelectDateWidget)
        #release = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))

        labels = {
            'title':'Title',
            'actor' : 'Star Actor',
            'director':'Movie Director',
            'writer': 'Movie Writer',
            'genre':'Genre',
            'country': 'Country',
            'rating': 'Rating',
            'score': 'Score',
            'year': 'Year',
            'release': 'Release',
            'runtime':'Runtime'
        }

    def __init__(self, *args, **kwargs):
        super(MovieForm,self).__init__(*args, **kwargs)
        self.fields['title'].empty_label = "Please insert the movie title"
        self.fields['score'].required = False
        self.fields['runtime'].required = False
        self.fields['score'].required = False
        self.fields['rating'].required = False
        self.fields['release'].required = False
        self.fields['genre'].empty_label ="Select"
        self.fields['score'].empty_label ="Select"
        self.fields['year'].empty_label ="Select"
        self.fields['country'].empty_label ="Select"
        self.fields['release'].widget = AdminDateWidget()


