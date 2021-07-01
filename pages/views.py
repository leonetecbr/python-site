from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  content = {
    'text': "",
  }
  response = HttpResponse(template.render(content, request))
  return response