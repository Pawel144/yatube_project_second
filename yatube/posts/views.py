from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    html_content = '<html><head><title>Анфиса для друзей</title></head><body>'
    html_content += '<h1>Главная страница</h1>'
    html_content += '</body></html>'    
    return HttpResponse(html_content) 