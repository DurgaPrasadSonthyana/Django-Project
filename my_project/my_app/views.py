from django.http import HttpResponse
from django.template import loader

def my_app(request):
  template = loader.get_template('first.html')
  return HttpResponse(template.render())