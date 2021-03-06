from django.shortcuts import render
from webapp.models import Article


def index_view(request):
    data = Article.objects.all()

    return render(request, 'index.html', context={
        'article': data
    })

def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        context = {
            'title': request.POST.get('title'),
            'content': request.POST.get('content'),
            'author': request.POST.get('author')
        }
        return render(request, 'article_view.html', context)
# Create your views here.
