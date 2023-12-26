

# views.py
from django.http import HttpResponseBadRequest

from django.shortcuts import render,HttpResponse,redirect
from myapp.models import Report,Report_Detail
from .models import Report, Report_Detail
from .forms import Report_DetailForm ,PatientForm # Import the Report_DetailForm
import json
from django.http import JsonResponse


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
   return render(request,'AvailableTest.html')

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
    
    options = {
        "Complete Blood Count (CBC)": [
          { "text": 'Red Blood Cell Count (RBC)', "reference": '4.5 - 5.5 million', "unit": 'cells/mcL' },
          { "text": 'Hemoglobin (Hb)', "reference": '12.0 - 15.5', "unit": 'g/dL' },
          { "text": 'Hematocrit (Hct)', "reference": '38.3% - 48.6%', "unit": '' },
          { "text": 'White Blood Cell Count (WBC)', "reference": '4,000 - 11,000', "unit": 'cells/mcL' },
          { "text": 'Platelet Count', "reference": '150,000 - 450,000', "unit": 'cells/mcL' }
        ],
        "Blood Glucose": [
          { "text": 'Fasting Blood Glucose', "reference": '70 - 99', "unit": 'mg/dL' }
        ],
        "Lipid Panel": [
          { "text": 'Total Cholesterol', "reference": 'Less than 200', "unit": 'mg/dL' },
          { "text": 'LDL Cholesterol', "reference": 'Less than 100', "unit": 'mg/dL' },
          { "text": 'HDL Cholesterol', "reference": '40 - 60', "unit": 'mg/dL' },
          { "text": 'Triglycerides', "reference": 'Less than 150', "unit": 'mg/dL' }
        ],
        "Liver Function Tests": [
          { "text": 'ALT (Alanine Aminotransferase)', "reference": '7 - 56', "unit": 'U/L' },
          { "text": 'AST (Aspartate Aminotransferase)', "reference": '5 - 40', "unit": 'U/L' },
          { "text": 'ALP (Alkaline Phosphatase)', "reference": '44 - 147', "unit": 'U/L' },
          { "text": 'Total Bilirubin', "reference": '0.3 - 1.2', "unit": 'mg/dL' }
        ],
        "Kidney Function Tests": [
          { "text": 'BUN (Blood Urea Nitrogen)', "reference": '7 - 20', "unit": 'mg/dL' },
          { "text": 'Serum Creatinine', "reference": '0.6 - 1.3', "unit": 'mg/dL' }
        ],
        "Electrolytes": [
          { "text": 'Sodium', "reference": '135 - 145', "unit": 'mmol/L' },
          { "text": 'Potassium', "reference": '3.5 - 5.0', "unit": 'mmol/L' },
          { "text": 'Chloride', "reference": '98 - 108', "unit": 'mmol/L' }
        ],
        "Thyroid Function Tests": [
          { "text": 'TSH (Thyroid Stimulating Hormone)', "reference": '0.4 - 4.0', "unit": 'mIU/L' },
          { "text": 'FT4 (Free Thyroxine)', "reference": '0.8 - 1.8', "unit": 'ng/dL' }
        ],
        "Iron Studies": [
          { "text": 'Serum Iron', "reference": '65 - 176', "unit": 'µg/dL' },
          { "text": 'TIBC (Total Iron Binding Capacity)', "reference": '250 - 450', "unit": 'µg/dL' },
          { "text": 'Ferritin', "reference": '12 - 300', "unit": 'ng/mL' }
        ],
        "C-Reactive Protein (CRP)": [
          { "text": '', "reference": 'Less than 0.8', "unit": 'mg/dL' }
        ],
        "Uric Acid": [
          { "text": 'Male', "reference": '3.4 - 7.0', "unit": 'mg/dL' },
          { "text": 'Female', "reference": '2.4 - 6.0', "unit": 'mg/dL' }
        ]}

    if request.method == 'POST':
      
        patient_name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        lab_no = request.POST.get('lab_no')
        contact = request.POST.get('contact')
        date = request.POST.get('date')
        consultant = request.POST.get('consultant')

        # Perform basic validation
        if age.strip() == '' or not age.isnumeric():
            return render(request, 'createReport.html', {'options': options})

        new_report = Report(
            patient_Name=patient_name,
            age=age,
            gender=gender,
            address=address,
            lab_no=lab_no,
            contact=contact,
            date=date,
            consultant=consultant
        )
        new_report.save()
      
        test_dropdown = request.POST.get('test_list')
        if test_dropdown:
            
            if test_dropdown in options:
                subtests = options[test_dropdown]
                for subtest in subtests:
                    text = subtest['text']
                    # result = request.POST.get(f'{text}_result')
                    result ="ok"
                    reference = subtest['reference']
                    unit = subtest['unit']

                    new_report_detail = Report_Detail(
                        report=new_report,
                        test_list=test_dropdown,
                        investigation=text,
                        results=result,
                        reference_value=reference,
                        unit=unit
                    )
                    new_report_detail.save()

                return HttpResponse("Report created successfully")
            else:
                return HttpResponse("Invalid test selected. ")
        else:
           return HttpResponse("empty. ")
    else:
      form = Report_DetailForm()
    return render(request, 'createReport.html')



def viewreport(request):
    return render(request,'viewreport.html')


def packages(request):
    return render(request,'packages.html')

def techlogin(techlogin):
    return render(request ,"techlogin.html")




    if request.method == 'POST':
        # Use request.POST to get data from a POST request
        patient_Name = request.POST.get('patient_Name', '')
        contact = request.POST.get('contact', '')

        print(f"Patient Name: {patient_Name}, Contact: {contact}")

        # Assuming you want to fetch data where patient_name is "test" and contact is "5151645"
        report_data = Report.objects.filter(patient_Name=patient_Name, contact=contact).first()
        report_detail_data = Report_Detail.objects.all()

        if report_data is not None:
            # Process the data
            print("Data found")
        else:
            # Handle the case when no data is found
            print("No data found")

        context = {
            'report_data': report_data,
            'report_detail_data': report_detail_data,
        }

        return render(request, 'test.html', context)

    return HttpResponse('Invalid request')
def test(request):
    if request.method == 'POST':
        patient_Name = request.POST.get('patient_Name', '')
        contact = request.POST.get('contact', '')

        print(f"Patient Name: {patient_Name}, Contact: {contact}")

        if contact:
            report_data = Report.objects.filter(patient_Name=patient_Name, contact=contact).first()
            report_detail_data = Report_Detail.objects.filter(report_id=report_data.id)
            print(report_data)

            if report_data is not None:
                print("Data found")
            else:
                print("No data found")

            context = {
                'report_data': report_data,
                'report_detail_data': report_detail_data,
            }
            print(f"Method: {request.method}")
            print(f"Contact: {contact}")

            return render(request, 'test.html', context)

        return HttpResponse('Invalid request or empty contact field')
    
# def test(request):
#     if request.method == 'POST':
#         # Use request.POST to get data from a POST request
#         patient_Name = request.POST.get('patient_Name', '')
#         contact = request.POST.get('contact', '')

#         print(f"Method: {request.method}")
#         print(f"Patient Name: {patient_Name}, Contact: {contact}")

#         # Check if contact is not an empty string before using it in the filter
#         if contact:
#             # Assuming you want to fetch data where patient_name is "test" and contact is a non-empty string
#             report_data = Report.objects.filter(patient_Name=patient_Name, contact=contact).first()
#             report_detail_data = Report_Detail.objects.all()
#             print(report_data)

#             if report_data is not None:
#                 # Process the data
#                 print("Data found")
#             else:
#                 # Handle the case when no data is found
#                 print("No data found")

#             context = {
#                 'report_data': report_data,
#                 'report_detail_data': report_detail_data,
#             }

#             return render(request, 'test.html', context)

#     elif request.method == 'GET':
#         # Use request.GET to get data from a GET request
#         patient_Name = request.GET.get('patient_Name', '')
#         contact = request.GET.get('contact', '')

#         print(f"Method: {request.method}")
#         print(f"Patient Name: {patient_Name}, Contact: {contact}")

#         # You can add logic here to handle the GET request data

#         return HttpResponse('GET request received')
#         # return render(request, 'test.html', context)

#     # Return a default response if neither POST nor GET conditions are met
#
#      return HttpResponse('Invalid request or empty contact field')



# def userlogin(request):
#     if request.method == 'POST':
#         patient_Name = request.POST.get('patient_Name', '')
#         contact = request.POST.get('contact', '')
#         form = PatientForm(request.POST)
#         print(f"Method: {request.method}")
#         print(f"Patient Name: {patient_Name}, Contact: {contact}")
#         if form.is_valid():
#             patient_name = form.cleaned_data['patient_Name']
#             contact = form.cleaned_data['contact']

#             # Check if the patient exists in the database
#             if Report.objects.filter(patient_Name="Srijan", contact="9862107925").exists():
#                 # Redirect to the test page
#                 return redirect('test')  # Replace 'test_page_url_name' with the actual URL name of your test page
#             else:
#                 # Patient not found, handle accordingly (e.g., show an error message)
#                 pass
#     else:
#         form = PatientForm()

#     return render(request, 'test.html', {'form': form})

def userlogin(request):
    return render(request,'userlogin.html')