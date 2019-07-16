from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
   #return HttpResponse('THIS IS A Test :Hello from Home Page')
  
    return render(request, 'CupCakeCode/home.html')