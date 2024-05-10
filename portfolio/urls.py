from django.urls import path
from . import views

urlpatterns = [
    path('', views.empty, name='empty'),
    path('<str:email>', views.index, name='index'),
]
