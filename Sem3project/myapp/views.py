from django.shortcuts import render,HttpResponse
from .models import Report  # Import the Report model
from .forms import Report_DetailForm  # Import the Report_DetailForm

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
        # consultant = request.POST.get('consultant')
        # investigation = request.POST.get('investigation')
        # results = request.POST.get('results')
        # reference_value = request.POST.get('reference_value')
        # unit = request.POST.get('unit')
        
        
        # Create a new Report instance and save it to the database
        new_report = Report(
            patient_Name=patient_Name,
            dispatch_date=dispatch_date,
            age=age,
            gender=gender,
            address =address,
            lab_no =lab_no,
            contact =contact,
            date =date
        #    consultant =consultant,
        #    investigation =investigation,
        #     results =results,
        #     reference_value =reference_value,
        #     unit =unit
            # Set other fields similarly
        )
        new_report.save()  # Save the report to the database
        return HttpResponse("Report created successfully")  # You can redirect or render a different page here
    else:
        return render(request, 'createReport.html')  # Render the createReport.html template for GET requests
  




# Your other views here...

def create_report_detail(request):
    if request.method == 'POST':
        form = Report_DetailForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return HttpResponse("Report detail created successfully")  # Success message or redirect
    else:
        form = Report_DetailForm()
    return render(request, 'createReport.html', {'form': form})
