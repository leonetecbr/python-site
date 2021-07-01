from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  content = {
    'text': 'Helloword',
  }
  response = HttpResponse(template.render(content, request))
  return response

def conta(request):
  template = loader.get_template('conta.html')
  content = {}
  response = HttpResponse(template.render(content, request))
  return response

