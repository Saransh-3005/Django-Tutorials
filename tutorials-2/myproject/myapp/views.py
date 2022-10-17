from django.shortcuts import render
from .models import Feature
# Create your views here.
def index(request):
    features=Feature.objects.all()
    return render(request, 'index.html',{'features':features})