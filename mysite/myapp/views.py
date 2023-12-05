from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context ={
        'variable':"this is sent"
    }
    return render(request,'homepage.html',context)

def about(request):
    return HttpResponse('This is my about')

def services(request):
    return HttpResponse('This is my service')