from django.shortcuts import render
from .models import  Place


# Create your views here.

def page1(request):
  obj= Place.objects.all()

  return render(request,"index2.html",{'result': obj})
