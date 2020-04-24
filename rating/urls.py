from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list, name='list'),
    path('ratinglist', views.ratinglist, name='ratinglist'),
    path('singlerating', views.rating, name='rating'),
    path('rate', views.rate, name='rate'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]
