from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def months(request):
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    context = {
        'months': months
    }

    return render(request, 'months.html', context)

def challenges(request):
    month = request.GET.get('month')

    challenges_for_month = get_challenges_for_month(month)

    context = {
        'challenges': challenges_for_month,
        'month': month
    }

    return render(request, 'challenges.html', context)

def get_challenges_for_month(month):  
    challenges_by_month = {
        'january': [ 'Improve Skills', 'Learn Everything Possible', 'Get a Job' ],
        'february': ['Eat Healthy', 'Workout','Get a Job'],
        'march': ['Make a Short Film', 'Learn from Movies', 'Develop out of box Stories', 'Get a Job'],
        'april': ['Complete reading Psychology of Money', 'Start Rich Dad Poor Dad', 'Get a Job'],
        'may': ['Get a Job', 'Get a Job for sure'],
        'june': ['Challenge 1 for June', 'Challenge 2 for June'],
        'july': ['Challenge 1 for July', 'Challenge 2 for July'],
        'august': ['Challenge 1 for august', 'Challenge 2 for august'],
        'september': ['Challenge 1 for september', 'Challenge 2 for september'],
        'october': ['Challenge 1 for october', 'Challenge 2 for october'],
        'november': ['Challenge 1 for november', 'Challenge 2 for november'],
        'december': ['Challenge 1 for december', 'Challenge 2 for december'],
    }
    
    challenges = challenges_by_month.get(month.lower(), [])  # Convert month name to lowercase for case-insensitive matching
    
    return challenges