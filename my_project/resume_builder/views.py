from django.shortcuts import redirect, render
from . import forms
from .forms import CreateResume
from .models import ResumeBuilder

def resume_form(request):
    if request.method == 'POST':
        form = forms.CreateResume(request.POST)
        if form.is_valid():
            # saves with user 
            newpost = form.save()
            newpost.author = request.user
            newpost.save()
            return redirect('resume_builder:resume')
    else:
        form = forms.CreateResume()
    return render(request, 'resume_builder/resume_form.html', {'form': form})

def resume(request):
    resumes = ResumeBuilder.objects.filter(author=request.user)
    return render(request, 'resume_builder/resume.html', {'resumes': resumes})
