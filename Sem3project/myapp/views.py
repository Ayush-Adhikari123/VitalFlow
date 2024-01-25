


import json

from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import HttpResponse, get_object_or_404, render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt

from myapp.models import (Contact, Feedback, Report, Report_Detail, TechAdd,
                          homeservice, technicianlogin)

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
   return render(request,'AvailableTest.html')

def report(request):
    return HttpResponse("This is Report Page")

def package(request):
    return HttpResponse("This is Package Page")

def feedback(request):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('feedback')
        
        new_feedback = Feedback(
                name=full_name,
                email=email,                
                message=message
            )
        new_feedback.save()
    return render(request,'feedback.html')

def about(request):
    return HttpResponse("This is About Page")

def contact(request):

     if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        message = request.POST.get('message')
        
        new_contact = Contact(
                full_name=full_name,
                email=email,
                contact=contact,
                message=message
            )
        new_contact.save()
        
        email_subject = 'New Contact Form Submission'
        email_message = f"Full Name: {full_name}\nEmail: {email}\nContact No.: {contact}\nMessage: {message}\nFor the Complete detail Click on the link>: http://127.0.0.1:8000/contactpannel"
        sender_email = 'rujanbhetwal65.com'  # Replace with your email
        recipient_email = 'vitalflow33@gmail.com'

        send_mail(
            email_subject,
            email_message,
            sender_email,
            [recipient_email],
            fail_silently=False,
        )

        success_message = "Data saved successfully in the database!"
        
        

        # Returning the success message as an HTTP response
        return HttpResponse(success_message)
            # return render(request, 'homeService.html') 
     else:       
        return render(request,'contactus.html')


def adminprofile(request):
    return render(request,'adminprofile.html')
      
def createreport(request):
    patient_name = request.POST.get('name')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    address = request.POST.get('address')
    lab_no = request.POST.get('lab_no')
    contact = request.POST.get('contact')
    date = request.POST.get('date')
    consultant = request.POST.get('consultant')
    test_dropdown = request.POST.get('test_list')
    investigation=request.POST.getlist('investigation[]')
    result = request.POST.getlist('result[]')
    reference=request.POST.getlist('references[]')
    unit=request.POST.getlist('unit[]')
    
    if request.method == 'POST':
      
        

        # Perform basic validation
        # if age.strip() == '' or not age.isnumeric():
        #     return render(request, 'createReport.html', {'options': options})

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
        
        #report_details
        num_investigations = len(investigation)
        
        # Run the loop for the number of elements in the investigation list
        for i in range(num_investigations):
            investigation_value = investigation[i]
            result_value = result[i]
            reference_value = reference[i]
            unit_value = unit[i]

            new_report_detail = Report_Detail(
                                report=new_report,  # Link the Report_Detail instance to the main report
                                test_list=test_dropdown,
                                investigation=investigation_value,
                                results=result_value,  # Use the current result value
                                reference_value=reference_value,
                                unit=unit_value
                            )
            new_report_detail.save()
    print(request.POST)
    # return JsonResponse(data={})
    return render(request, 'createReport.html')



def viewreport(request):
    return render(request,'viewreport.html')


def packages(request):
    return render(request,'packages.html')

def adminlogin(request):
    return render(request,"adminlogin.html")


# =====================================================================================

from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       SetPasswordForm, UserChangeForm)

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
        existing_report.lab_no = request.POST.get('lab_no')
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

        # Update Report_Detail records with the new result values
        result_values = request.POST.getlist('result_values')

        for i, report_detail in enumerate(report_details):
    # Check if there are enough values in result_values
            if i < len(result_values):
                result_value = result_values[i]
                # Update the results field
                report_detail.results = result_value
                report_detail.save()


        return HttpResponse("Report and Report_Detail updated successfully")
    
    
    elif request.method == 'GET':
        report_data = Report.objects.all()  # Fetch all data from Report model
        existing_report = get_object_or_404(Report, contact=contact)
        reportdetail_data = Report_Detail.objects.filter(report=existing_report)  # Fetch all data from Report model
        
        context = {
            'report_data': report_data,
            'reportdetail_data': reportdetail_data,
            'report': existing_report,  # Include the existing_report in the context
        }
        return render(request, 'updateReport.html', context)

    

def techlogin(request):
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
    


# def book_service(request):
#     return render(request,'homeService.html')

# ================================================================= tech profile
def techprofile(request):
      if request.method == "POST":
         fm= EditadminprofileForm(request.POST, instance= request.user)
         if fm.is_valid():
          messages.info(request,'Profile Updated Successfully!')
          fm.save()
      else:
          fm =EditadminprofileForm(instance=request.user)
      return render(request,'techprofile.html',{'name': request.user,'form':fm})
    
  
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
        
        if first_name.strip() == '' :
            error_message = "Please enter a valid first name."
            options = {}  # Define your 'options' here if needed
            return render(request, 'techadd.html', {'options': options, 'error_message': error_message})
          
        if last_name.strip() == '' :
            error_message = "Please enter a valid last name."
            options = {}  # Define your 'options' here if needed
            return render(request, 'techadd.html', {'options': options, 'error_message': error_message})
          
        if email.strip() == '' :
            error_message = "Please enter a valid email."
            options = {}  # Define your 'options' here if needed
            return render(request, 'techadd.html', {'options': options, 'error_message': error_message})
        if contact.strip() == '' :
            error_message = "Please enter a valid contact."
            options = {}  # Define your 'options' here if needed
            return render(request, 'techadd.html', {'options': options, 'error_message': error_message})

        if password.strip() == '' :
            error_message = "Please enter a valid password."
            options = {}  # Define your 'options' here if needed
            return render(request, 'techadd.html', {'options': options, 'error_message': error_message})

        if com_password.strip() == '' :
            error_message = "Please enter a valid confirm password."
            options = {}  # Define your 'options' here if needed
            return render(request, 'techadd.html', {'options': options, 'error_message': error_message})

        if password != com_password:
            messages.success(request,"Password didn't match")
            return render(request, 'techadd.html')

        if gender.strip() == '' :
            error_message = "Please enter a valid gender."
            options = {}  # Define your 'options' here if needed
            return render(request, 'techadd.html', {'options': options, 'error_message': error_message})

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
  

def techpannel(request):
  
  if request.method == 'GET':
        techadd_data = TechAdd.objects.all()  # Fetch all data from TechAdd model
        context = {
            'techadd_data': techadd_data,
        }
        return render(request, 'techpannel.html', context)
  else:
        return HttpResponse('Invalid request or empty contact field')
    



def book_home_service(request):
    if request.method == 'POST':
        # Get form data from POST request
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        location = request.POST.get('direction')
        description = request.POST.get('description')

        # Create a homeservice object and save it to the database
        service = homeservice(
            Name=name,
            Phonenumber=phone_number,
            Email=email,
            latitude=latitude,
            longitude=longitude,
            location=location,
            discription=description
        )
        service.save()

        # Redirect to a success page or any other desired page after saving

        return HttpResponseRedirect('gethomeservice')  # Redirect to a success page

    return render(request, 'homeService.html') 

       

    

def homeservicepannel(request):
    if request.method == 'GET':
        # Filter the data where 'done_column' is 0
        homeservice_data = homeservice.objects.filter(done=0)
        
        context = {
            'homeservice_data': homeservice_data,
        }
        return render(request, 'homeservicepannel.html', context)
    else:
        return HttpResponse('Invalid request or empty contact field')
  


def update_done_status(request, service_id,tempmail):
    if request.method == 'POST':
        hmservice = homeservice.objects.get(id=service_id)
        hmservice.done = 1  # Update the 'done' status to 1
        hmservice.save()

        full_name = hmservice.Name
        email = hmservice.Email
        contact = hmservice.Phonenumber
        lat = hmservice.latitude
        lng = hmservice.longitude
        location = hmservice.location
        discription = hmservice.discription

        #for sending the mail

        


        email_subject = 'New Home Service'
        html_message = render_to_string('servicelocation.html', {
            'full_name': full_name,
            'email': email,
            'contact': contact,
            'discription': discription,
            'location': location,
            'lat':lat,
            'lng':lng,
            
        })
        email_message = strip_tags(html_message)
        sender_email = 'vitalflow33@gmail.com'
        recipient_email = tempmail

        email = EmailMultiAlternatives(
            email_subject,
            email_message,
            sender_email,
            [recipient_email]
        )
        

        email.attach_alternative(html_message,"text/html")
        email.send()

        return render(request,'homeservicepannel.html')

    return JsonResponse({'message': 'Invalid request method'}, status=405)


def delete_service(request, service_id):
    if request.method == 'POST':
        hmservice = homeservice.objects.get(id=service_id)
        hmservice.delete()

        return render(request,'homeservicepannel.html')

    return JsonResponse({'message': 'Invalid request method'}, status=405)



       


#   ================================================srijan
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

def userlogin(request):
    return render(request,'userlogin.html')

def diagnostic(request):
    return render(request,'diagnostic.html')



def contactpannel(request):
  
  if request.method == 'GET':
        contact_data = Contact.objects.all()  # Fetch all data from TechAdd model
        context = {
            'contact_data': contact_data,
        }
        return render(request, 'contactpannel.html', context)
  else:
        return HttpResponse('Invalid request or empty contact field')
    
def delete_record(request, record_id):
    if request.method == 'POST':
        record = get_object_or_404(Contact, pk=record_id)
        record.delete()
        return JsonResponse({'message': 'Record deleted successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)




def feedbackpannel(request):
    if request.method == 'GET':
        
        feedback_data = Feedback.objects.filter(show=1)
        
        context = {
            'feedback_data': feedback_data,
        }

        return render(request, 'feedbackadmin.html', context)
    else:
        return HttpResponse('Invalid request or empty contact field')
    

def delete_feed(request, feed_id):
    if request.method == 'POST':
        feed = Feedback.objects.get(id=feed_id)
        feed.delete()

        return JsonResponse({'message': 'Record deleted successfully'}, status=200)

    return JsonResponse({'message': 'Invalid request method'}, status=405)