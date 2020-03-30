from django.urls import path,include


from . import views

urlpatterns = [
    path('insert/', views.movies_form,name='movies_insert'), # get and post req. for insert operation
    path('', views.home, name='movies_home'),
    path('movies/', views.movies , name='movies'),
    path('charts/', views.charts , name='charts'),
    path('<int:id>/', views.movies_form,name='movies_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.movies_delete,name='movies_delete'),
    path('list/',views.profile_upload,name='movies_list'), # get req. to retrieve and display all records
    path('about/', views.about, name='about'),
]

