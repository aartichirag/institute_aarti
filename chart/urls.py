from django.urls import path
from .views import chartdemo

urlpatterns=[
    path("chart/",chartdemo,name="chart")
]