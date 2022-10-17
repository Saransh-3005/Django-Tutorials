from itertools import count
from django.shortcuts import render
import django.http 
from .models import Feature
# from .models import Feature
# Create your views here.
def index (request):
    features=Feature.objects.all()
    return render(request , 'index.html', {'features':features})


def counter(request):
     return render(request,'counter.html')

def result(request):
    word=request.POST['text1']
    count=len(word.split())
    return render(request,'result.html',{"word":count})