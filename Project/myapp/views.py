from itertools import count
from django.shortcuts import render
import django.http 
from .models import Feature
# Create your views here.
def index (request):
    feature1 = Feature()
    feature1.featurId=1
    feature1.head = 'Fast'
    feature1.deatils= 'This is the feature of the This Website that It is very VERY Fast'

    feature2 = Feature()
    feature2.featurId=2
    feature2.head = 'Reliable'
    feature2.deatils= 'This  Website is Also Reliable as all the information on this is verified '

    feature3 = Feature()
    feature3.featurId=3
    feature3.head = 'Safe'
    feature3.deatils= 'This Site is also very Safe and Hacking proof '

    feature4 = Feature()
    feature4.featurId=4
    feature4.head = 'Secure'
    feature4.deatils= 'Security level of this Website is Exceptional and the security of this Website cannot be broken Easily'

    features=[feature1,feature2,feature3,feature4]
    return render(request , 'index.html',{'features':features})


def counter(request):
     word=request.POST['text1']
     count=len(word.split())
     return render(request,'counter.html',{"word":count})

    
# def index(request):
#     return render(request, 'sh.html')
