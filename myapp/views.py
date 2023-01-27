from django.http import HttpResponse
import string
from random import randrange, choices
from django.shortcuts import render

def main(request):
    data = {
        'article': randrange(1, 100),
        'slug_text': ''.join(choices(string.hexdigits, k=10))
    }
    return render(request, 'base/index.html', data)

def my_arcticles(request):
    return render(request, 'my_arcticles.html')

def arct_archive(request):
    return render(request, 'arct_archive.html')

def users(request, user_number=None):
    return render(request, 'users.html')

def article(request, article_number, slug_text=''):
    data = {
        'article': article_number,
        'text': slug_text
    }
    return render(request, 'article.html', data)
