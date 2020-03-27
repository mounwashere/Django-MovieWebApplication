from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField

from country_list import countries_for_language
# Create your models here.





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
    [(i, i) for i in range(1900, 2020)]
)

RATING = (
    [(i, i) for i in range(0, 10)]
)


class Movies(models.Model):
    title = models.CharField(max_length=120)
    actor = models.CharField(max_length=120)
    writer = models.CharField(max_length=120)
    genre = models.CharField(max_length=120, choices=GENRE)
    synopsis = models.CharField(max_length=5000, default="")
    country = CountryField(blank_label='Select country')
    director = models.CharField(max_length=120)
    rating = models.IntegerField(choices=RATING)
    score = models.IntegerField()
    year = models.IntegerField( choices=YEARS)
    release = models.DateField()
    runtime = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

