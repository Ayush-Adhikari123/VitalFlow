from django.shortcuts import render,HttpResponse
from .models import Report  # Import the Report model
from .models import technicianlogin
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

def about(request):
    return HttpResponse("This is About Page")

def contact(request):
    return HttpResponse("This is Contact Page")

def adminpage(request):
    return render(request,'adminpage.html')


def createreport(request):
    if request.method == 'POST':
        # Extract form data from the POST request
        patient_Name = request.POST.get('name')
        dispatch_date = request.POST.get('date')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        lab_no = request.POST.get('lab_no')
        contact = request.POST.get('contact')
        date = request.POST.get('date')
        consultant = request.POST.get('consultant')
        investigation = request.POST.get('investigation')
        results = request.POST.get('results')
        reference_value = request.POST.get('reference_value')
        unit = request.POST.get('unit')
        
        
        # Create a new Report instance and save it to the database
        new_report = Report(
            patient_Name=patient_Name,
            dispatch_date=dispatch_date,
            age=age,
            gender=gender,
            address =address,
            lab_no =lab_no,
            contact =contact,
            date =date,
           consultant =consultant,
           investigation =investigation,
            results =results,
            reference_value =reference_value,
            unit =unit
            # Set other fields similarly
        )
        new_report.save()  # Save the report to the database
        return HttpResponse("Report created successfully")  # You can redirect or render a different page here
    else:
        return render(request, 'createReport.html')  # Render the createReport.html template for GET requests


def createtechnicianlogin(request):
    if request.method == 'POST':
        # Extract form data from the POST request
        technician_id = request.POST.get('technician_id')
        Password = request.POST.get('Password')

        new_technicianlogin= technicianlogin(
            technician_id=technician_id,
            Password=Password
        )
        new_technicianlogin.save()
        return HttpResponse("Succesfully Logined")
    else:
        return render(request,'techlogin.html')
    

def createadminpage(request):
    if request.method == 'POST':
        # Extract form data from the POST request
        admin_id = request.POST.get('admin_id')
        Password = request.POST.get('Password')

        new_adminpage= adminpage(
            admin_id=admin_id,
            Password=Password
        )
        new_adminpage.save()
        return HttpResponse("Succesfully Logined")
    else:
        return render(request,'adminpage.html')

