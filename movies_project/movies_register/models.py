import numpy
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField

from country_list import countries_for_language
# Create your models here.



class Document(models.Model):
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    #upload_by = models.ForeignKey('auth.User', related_name='uploaded_documents')

    class Meta:
        db_table = 'Document'



GENRE = (
    ('Action', 'Action'),
    ('Aventure', 'Adventure'),
    ('Animation', 'Animation'),
    ('Biography', 'Biography'),
    ('Comedie', 'Comedy'),
    ('Crime', 'Crime'),
    ('Drama', 'Drama'),
    ('Famille', 'Family'),
    ('Musical', 'Musical'),
    ('Mystere', 'Mystery'),
    ('Romance', 'Romance'),
    ('Science-Fiction', 'Science-Fiction'),
    ('Guerre', 'War'),
    ('Western', 'Western')
)



YEARS = (
    [(i, i) for i in range(1899, 2021)]
)




class Movies(models.Model):
    title = models.CharField(max_length=120)
    actor = models.CharField(max_length=120)
    writer = models.CharField(max_length=120)
    genre = models.CharField(max_length=120, choices=GENRE)
    country = models.CharField(max_length=120)
    director = models.CharField(max_length=120)
    rating = models.CharField(max_length=120)
    score = models.FloatField()
    year = models.IntegerField( choices=YEARS)
    release = models.DateTimeField(blank=True, default='', null=True)
    runtime = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

