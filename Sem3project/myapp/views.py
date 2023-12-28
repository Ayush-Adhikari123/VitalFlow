

# views.py
from django.shortcuts import render,HttpResponse
from myapp.models import Report,Report_Detail,TechAdd
from .forms import Report_DetailForm  # Import the Report_DetailForm
import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404

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

def adminprofile(request):
    return render(request,'adminprofile.html')
      
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

def adminlogin(request):
    return render(request,"adminlogin.html")


# =====================================================================================

from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib  import  messages
from .forms import EditadminprofileForm, EditsuperadminprofileForm
# login function for admin
def admin_login(request):
  if not request.user.is_authenticated:
    if request.method =="POST":
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
          uname = fm.cleaned_data['username']
          upass = fm.cleaned_data['password']
          user = authenticate(username=uname,password=upass)
          if user is not None:
              login(request,user)
              messages.success(request,'LOGED IN SUCCESSFULLY🤯🤯🤯')
              return HttpResponseRedirect('/adminprofile/')
    else:
      fm=AuthenticationForm()
    return render(request,'adminlogin.html',{'form':fm})
  else:
      return HttpResponseRedirect('/adminprofile/')
  

def admin_profile(request):
    if  request.user.is_authenticated:
      if request.method == "POST":
         fm= EditadminprofileForm(request.POST, instance= request.user)
         if fm.is_valid():
          messages.info(request,'Profile Updated Successfully!')
          fm.save()
      else:
        # if request.user.is_superuser == True:
        #   fm =EditsuperadminprofileForm(instance = request.user)
        # else:
          fm =EditadminprofileForm(instance=request.user)
      return render(request,'adminprofile.html',{'name': request.user,'form':fm})
    else:
        return HttpResponseRedirect('adminlogin')



def admin_logout(request):
    logout(request)
    return HttpResponseRedirect("/adminlogin/")

def admin_password(request):
  if request.user.is_authenticated:  
    if request.method == "POST":
      fm = PasswordChangeForm(user=request.user,data = request.POST)
      if fm.is_valid():
          fm.save()
          # update_session_auth_hash(request,fm.user) =============> if uncommented, the admin will not be forcefully loged out .he will be movw to admin profile.
          messages.info(request,"PASSWORD HAS BEEN UPDATED!")
          return HttpResponseRedirect('/adminprofile/')
    else :
      fm = PasswordChangeForm(user=request.user)
    return render(request,'adminpassword.html',{'form': fm})
  else:
     return HttpResponseRedirect('/adminlogin/')
  

  # =========================================================================================
def updatereport(request,contact):
    if request.method == 'POST':
        # Retrieve the existing record from the database
        existing_report = get_object_or_404(Report, contact=contact)
        
        # Update the fields with the new values from the form
        existing_report.patient_Name = request.POST.get('name')
        existing_report.age = request.POST.get('age')
        existing_report.gender = request.POST.get('gender')
        existing_report.address = request.POST.get('address')
        existing_report.contact = request.POST.get('contact')
        existing_report.date = request.POST.get('date')
        existing_report.consultant = request.POST.get('consultant')

        # Perform basic validation on the updated age
        new_age = request.POST.get('age')
        if new_age.strip() == '' or not new_age.isnumeric():
            return render(request, 'updateReport.html', {'report': existing_report})

        # Save the updated record
        existing_report.save()
        
        
        # Retrieve Report_Detail records related to the Report
        report_details = Report_Detail.objects.filter(report=existing_report)

        # Update Report_Detail records
        for report_detail in report_details:
            investigation_name = report_detail.investigation  # Retrieve the investigation name

            # Get the updated result from the form using the input name
            result = request.POST.get(f'result_{existing_report.contact}_{investigation_name.replace(" ", "_")}')

            # Update the result in the Report_Detail model
            report_detail.results = result

            # Save the updated Report_Detail record
            report_detail.save()

        return HttpResponse("Report and Report_Detail updated successfully")
    else:
        # Retrieve the existing Report record for rendering in the form
        existing_report = get_object_or_404(Report, contact=contact)
        return render(request, 'updateReport.html', {'report': existing_report})
      
      
def techadd(request):
  if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        com_password = request.POST.get('com_password')
        gender = request.POST.get('gender')

        new_techadd = TechAdd(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            contact=contact,
            password=password,
            com_password=com_password,
            gender=gender
        )
        new_techadd.save()
        return HttpResponse("New technician added successfully")
  else:
      
    return render(request, 'techadd.html')