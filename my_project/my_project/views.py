# from django.http import HttpResponse
from django.shortcuts import redirect, render

def homepage(request):
    if request.user.is_authenticated:
        return redirect('/about')  
    # return HttpResponse("Home Page")
    return render(request,'home.html')

def about(request):
    # return HttpResponse("My About page")
    return render(request,'about.html')
