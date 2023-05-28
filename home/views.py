from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')


def test(request):

    # Page from the theme 
    return render(request, 'home/test.html')
