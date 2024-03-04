from django.shortcuts import render
from . models import travel

def index(request):
    obj=travel.objects.all()
    return render(request,"index.html",{'result':obj})
# Create your views here.
