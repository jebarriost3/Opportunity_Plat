from django.urls import path
from . import views

urlpatterns = [
    path('',views.egresado, name='egresado'),
]