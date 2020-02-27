from django.urls import path, include
from quizapp.api import RegisterAPI
from knox import views as knox_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/auth/',include('knox.urls')),
    path('api/auth/register/',RegisterAPI.as_view()),
]
