from django.urls import path
from . import views

urlpatterns = [
    path('my_app/', views.my_app , name='my_app'),
]