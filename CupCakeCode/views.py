from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
   #return HttpResponse('THIS IS A Test :Hello from Home Page')
  
    return render(request, 'CupCakeCode/home.html')


def about(request):
   return render(request, 'CupCakeCode/about.html')

def info(request):
   return render(request, 'CupCakeCode/info.html')

def cup_cake(request):
   #return render(request, 'CupCakeCode/cup_cake_app.html')
   return HttpResponse('THIS IS A Test :Hello from cup cake app Page')

def contact(request):
   return render(request, 'CupCakeCode/contact.html')