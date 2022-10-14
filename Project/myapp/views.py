from itertools import count
from django.shortcuts import render
import django.http 
# Create your views here.
def index (request):
    return render(request , 'index.html')


def counter(request):
     word=request.POST['text1']
     count=len(word.split())
     return render(request,'counter.html',{"word":count})

    
# def index(request):
#     return render(request, 'sh.html')
