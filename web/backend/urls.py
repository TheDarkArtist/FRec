from django.urls import path

from .views import *

urlpatterns  = [
    path('', root_endpoint),
]