
from django.urls import include, path
from . import views 
from . views import *


urlpatterns = [
    path('', views.home),
    path('home', views.home,name='home'),
    path('home/', views.home,name='home'),
    path('nedv', views.nedv,name='nedv'),
    path('nedv/', views.nedv,name='nedv'),
    
    path('nedv/<int:obyav_id>/', get_obyav, name = 'obyav'),

    path('export-xls', export_to_exel, name = 'export-xls'),

    path('register', views.register, name='register'),

    path('new', views.new, name = 'new'),
]

