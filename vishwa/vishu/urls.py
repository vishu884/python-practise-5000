from django.urls import path
from . import views
urlpatterns=[
    path('jadu/',views.home,name='home')
]