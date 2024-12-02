from ride.views import *
from django.urls import path
app_name='anything'

urlpatterns=[
    path('auto/',auto,name='auto'),
]

