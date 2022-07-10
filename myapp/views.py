from django.shortcuts import render
from django.template import loader  
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.http import JsonResponse
from .models import Dates
@csrf_exempt



class DateForm(forms.Form):
   date = forms.DateField(widget=forms.DateInput(attrs={'id':'date',"type":"date"}))
   days = forms.IntegerField()
   def save(self):
      data=self.data
      modelRef=Dates(date=data['date'],days=data['days'])
      modelRef.save()

def price(day):
    if day%7 == 0:
        cost = 200*day/7
    else:
        cost = day*33
    return cost


def view_function(request):
   if request.method =="POST":
      form= DateForm(request.POST)
      if form.is_valid():
         print("yesssssssssssss")
         date = form.cleaned_data['date']
         days = form.cleaned_data['days']
         print(price(days))
         form.save()
         return JsonResponse({"reply":"Your price is " + str(price(days))})
   
# Create your views here.
def index(request):
    form = DateForm()
    return render(request, "index.html",{"form":form})

