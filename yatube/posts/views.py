from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # html_content = '<html><head><title>Анфиса для друзей</title></head><body>'
    # html_content += '<h1>Главная страница отображается из views</h1>'
    # html_content += '</body></html>'    
    # return HttpResponse(html_content)
    template = 'posts/index.html'
    return render(request, template) 

def group_posts(request):
    template = 'posts/group_list.html'
    return render(request, template)
    # return HttpResponse(f'Мороженое номер {slug}')