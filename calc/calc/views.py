from django.shortcuts import render    
from django.http import HttpResponse  
import json  
import math

def index(request):
    return render(request, 'index.html')


def si(request):
    number1=  request.GET.get('num1')
    number2= request.GET.get('num2')
    number3= request.GET.get('num3')
    result=int(number1) * int(number2) * int(number3)/100

    res={
        "Simple Interest": result
    }
    return HttpResponse(json.dumps(res))


def ci(request):
    number1=  request.GET.get('num1')
    number2= request.GET.get('num2')
    number3= request.GET.get('num3')
    result=float(number1)*(1+float(number2)*float(number3))

    res={
        "Compound Interest": result
    }
    return HttpResponse(json.dumps(res))    

def emi(request):
    number1= request.GET.get('num1')
    number2= request.GET.get('num2')
    number3= request.GET.get('num3')
    r=float(number2)/(12*100)
    result=float(number1)*r*((1+r)**float(number3))/((1+r)**float(number3)-1)
    res={
        "monthlyemi": result
    }
    return HttpResponse(json.dumps(res))

def sip(request):
     number1= request.GET.get('num1')
     number2=request.GET.get('num2')
     number3=request.GET.get('num3')
     monthly=float(number2)/12/100
     result=float(number1)*((((1+monthly)**float(number3))-1)*(1+monthly))/monthly
    
     res={
          "sip": result
      }
     return HttpResponse(json.dumps(res))

def fd(request):
    number1= request.GET.get('num1')
    number2= request.GET.get('num2')
    number3= request.GET.get('num3')
    result=float(number1)+((float(number1)*(float(number2))*float(number3)/100))
    res={
        "fd":result
    }
    return HttpResponse(json.dumps(res))

def rd(request):
    number1= request.GET.get('num1')
    number2= request.GET.get('num2')
    number3= request.GET.get('num3')
    result=float(number1)*(1+float(number2)/4)**(4*float(number3)) 
    res={
        "rd":result
    }   
    return HttpResponse(json.dumps(res))

def pf(request):
    number1=request.GET.get('num1')    
    number2=request.GET.get('num2') 
    number3=request.GET.get('num3')
    result=int(number1)[(int(number2)+1)**int(number3)-1/int(number2)]
    res={
        "pf": result
    }
    return HttpResponse(json.dumps(res))

def lumpsum(request):
    number1=request.GET.get('num1')
    number2=request.GET.get('num2')
    number3=request.GET.get('num3')
    result=float(number1)*(1+float(number2))**float(number3)
    res={
        "lumpsum":result
    }
    return HttpResponse(json.dumps(res))