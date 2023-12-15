from django.shortcuts import render,HttpResponse
from .models import Report ,Report_Detail # Import the Report model
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


# def createreport(request):
#     if request.method == 'POST':
#         # Extract form data from the POST request
#         patient_Name = request.POST.get('name')
        
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')
#         address = request.POST.get('address')
#         lab_no = request.POST.get('lab_no')
#         contact = request.POST.get('contact')
#         date = request.POST.get('date')
#         consultant = request.POST.get('consultant')
#         # investigation = request.POST.get('investigation')
#         # results = request.POST.get('results')
#         # reference_value = request.POST.get('reference_value')
#         # unit = request.POST.get('unit')
        
        
#         # Create a new Report instance and save it to the database
#         new_report = Report(
#             patient_Name=patient_Name,
            
#             age=age,
#             gender=gender,
#             address =address,
#             lab_no =lab_no,
#             contact =contact,
#             date =date,
#            consultant =consultant
#         #    investigation =investigation,
#         #     results =results,
#         #     reference_value =reference_value,
#         #     unit =unit
#             # Set other fields similarly
#         )
#         new_report.save()  # Save the report to the database
#     #     return HttpResponse("Report created successfully")  # You can redirect or render a different page here
#     # else:
#     #     return render(request, 'createReport.html')  # Render the createReport.html template for GET requests
  




# # Your other views here...

# def create_report_detail(request):
#     if request.method == 'POST':
#         form = Report_DetailForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the form data to the database
#             return HttpResponse("Report detail created successfully")  # Success message or redirect
#     else:
#         form = Report_DetailForm()
#     return render(request, 'createReport.html', {'form': form})


# views.py


def createreport(request):
    if request.method == 'POST':
        # Extract form data from the POST request for Report model
        patient_name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        lab_no = request.POST.get('lab_no')
        contact = request.POST.get('contact')
        date = request.POST.get('date')
        consultant = request.POST.get('consultant')
        
        # Create a new Report instance and save it to the database
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
        new_report.save()  # Save the report to the database
        
        return HttpResponse("Report detail created successfully")  # Success message or redirect
    else:
        form = Report_DetailForm()
    return render(request, 'createReport.html', {'form': form})
        
def create_report_detail(request):
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
        # Save investigation-related data to the database
        test_dropdown = request.POST.get('testDropdown')
        if test_dropdown in options:
            subtests = options[test_dropdown]
            for subtest in subtests:
                text = subtest['text']
                result = request.POST.get(text)
                reference = subtest['reference']
                unit = subtest['unit']

                # Create and save Investigation instances related to the report
                new_Report_Detail = Report_Detail(
                    
                    investigation=text,
                    result=result,
                    reference_value=reference,
                    unit=unit
                )
                new_Report_Detail.save()

        return HttpResponse("Report created successfully")  # Redirect or render a different page here
    else:
        return render(request, 'createReport.html', {'options': options})