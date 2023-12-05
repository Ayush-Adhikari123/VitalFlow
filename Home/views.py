
from django.shortcuts import render, HttpResponse 

# Create your views here.
def index(request):
    context={
        "variable1":"srijan is great"
    }
    return render(request,'index.html',context)

def home(request):
    return HttpResponse("This is Home Page")

def availabletest(request):
    return HttpResponse("This is Available Test Page")

def report(request):
    return HttpResponse("This is Report Page")

def package(request):
    return HttpResponse("This is Package Page")

def feedback(request):
    return HttpResponse("This is Feedback Page")
