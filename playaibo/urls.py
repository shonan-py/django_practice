from django.urls import path

from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('forecast', views.ForecastView.as_view(), name='forecast'),
]
