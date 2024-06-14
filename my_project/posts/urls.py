from django.urls import include,path
from . import views

app_name = 'posts'

urlpatterns = [
    path('list/',views.posts_list, name="list"),
    path('new-post/',views.post_new, name="new-post"),
    path('<slug:slug>',views.post_page, name="page"),
]