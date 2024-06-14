from django.urls import path

from . import views

urlpatterns = [
    path('months/', views.months, name='months'),
    path('challenges/',views.challenges , name='challenges')
]
