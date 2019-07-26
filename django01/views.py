from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def SayHello(requist):
    return HttpResponse("hello World")

def AddWithDZF(requist):
    a = requist.GET.get("a")
    b = requist.GET.get("b")
    c = int(a) + int(b)
    return HttpResponse(str(c))

def AddWithDZF1(requist,a,b):
    c = int(a) + int(b)
    return HttpResponse("this is from addWithDZF1:" + str(c))

def nameindex(requist):
   return render(requist,"index.html")

def AddWithDZF2(requist,a,b):
    c = int(a) + int(b)
    return HttpResponse("this is from addWithDZF2:" + str(c))

def namefunctionshili(requist):
   return HttpResponseRedirect(reverse("usenameTest",args=(4/5)))