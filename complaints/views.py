from pydoc import describe
from unicodedata import category
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import UserRegistrationForm,UserPofileForm,UserComplaintForm
from django.views import View
from django.contrib import messages
from .models import Complainant,Complaint,Progress

# Create your views here.
 
def index(request):
    return render(request,"complaints/home.html")


class UserRegistrationView(View):
    def get(self,request):
        form = UserRegistrationForm()
        return render(request,"complaints/registration.html",{
            "form":form
        })
    
    def post(self,request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulations!! Registered Successfully!!")
            form.save()
        return render(request,"complaints/registration.html",{
            "form":form
        })



class ProfileView(View):
    def get(self,request):
        form = UserPofileForm()
        return render(request,"complaints/profile.html",{
            "form":form,
            "active" : "btn-primary"
        })

    def post(self,request):
        form = UserPofileForm(request.POST)
        if form.is_valid():
            user = request.user
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            street = form.cleaned_data["street"]
            city = form.cleaned_data["city"]
            postal_code = form.cleaned_data["postal_code"]
            reg = Complainant(user=user,first_name=first_name,last_name=last_name,street=street,city=city,postal_code=postal_code)
            reg.save()
            messages.success(request,"Congratulations!! Profile Created Successfully!!")

        return render(request,"complaints/profile.html",{
            "form":form,
            "active" : "btn-primary"
        })


def address(request):
    address = Complainant.objects.filter(user=request.user)
    return render(request,"complaints/address.html",{
        "address":address,
        "active" : "btn-primary"
    })


class UserComplaintView(View):
    def get(self,request):
        form = UserComplaintForm()
        return render(request,"complaints/complaint.html",{
            "form":form,
            "active" : "btn-primary"
        })
    
    def post(self,request):
        form = UserComplaintForm(request.POST)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data["title"]
            describe = form.cleaned_data["describe"]
            category = form.cleaned_data["category"]
            
            reg = Complaint(user=user,title=title,describe=describe,category=category)
            reg.save()
            messages.success(request,"Congratulations!! Profile Created Successfully!!")
        return render(request,"complaints/complaint.html",{
            "form":form,
            "active" : "btn-primary"            
        })


def allcomplaints(request):
    user = request.user
    address = Complainant.objects.filter(user=user)
    complaint = Complaint.objects.filter(user=user)
    return render(request,"complaints/complaint_confirm.html",{
        "address" : address,
        "complaint" : complaint 
    })

def complaintregistered(request):
    print("hellow")
    user = request.user
    userid = request.GET.get("userid")
    complainant = Complainant.objects.get(id=userid)
    complaint = Complaint.objects.filter(user=user)
    print(user,userid,complainant,complaint)
    for c in complaint:
       print(c)
       Progress(user=user,complainant=complainant,title=c.title,describe=c.describe,category=c.category).save()
       c.delete()
    return redirect("complaintstatus")


def complaintstatus(request):
    complaintant = Progress.objects.filter(user=request.user)
    return render(request,"complaints/complaint_status.html",{
        "complaintant" : complaintant
    })