from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'article/index.html', context)

def article(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {'article': article}
    return render(request, 'article/article.html', context)