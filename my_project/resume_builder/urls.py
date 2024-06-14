from django.urls import path
from . import views

app_name = 'resume_builder'

urlpatterns = [
    path('resume_form/',views.resume_form, name="resume_form"),
    path('resume/',views.resume, name="resume"),
]