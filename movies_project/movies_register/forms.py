from django import forms
from .models import  Movies
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from movies_project import settings
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import widgets

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movies
        fields = ('title', 'actor','director', 'writer', 'genre' ,'synopsis', 'country', 'rating', 'score','year','release',  'runtime')
        country = CountryField().formfield()
        #release1 = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, label='What is the date of release?', widget=forms.SelectDateWidget)
        #release = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))

        labels = {
            'title':'Title',
            'actor' : 'Star Actor',
            'director':'Movie Director',
            'writer': 'Movie Writer',
            'genre':'Genre',
            'synopsis':'Synopsis',
            'country': 'Country',
            'rating': 'Rating',
            'score': 'Score',
            'year': 'Year',
            'runtime':'Runtime'
        }

    def __init__(self, *args, **kwargs):
        super(MovieForm,self).__init__(*args, **kwargs)
        self.fields['title'].empty_label = "Please insert the movie title"
        self.fields['score'].required = False
        self.fields['synopsis'].required = False
        self.fields['synopsis'].widget.attrs.update(size='100')
        self.fields['runtime'].required = False
        self.fields['score'].required = False
        self.fields['rating'].required = False
        self.fields['release'].required = False
        self.fields['genre'].empty_label ="Select"
        self.fields['rating'].empty_label ="Select"
        self.fields['year'].empty_label ="Select"
        self.fields['country'].empty_label ="Select"
        self.fields['release'].widget = AdminDateWidget()


