from django.shortcuts import render

# Create your views here.
import datetime
from django.contrib import messages

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from Attendance.EmailBackEnd import EmailBackEnd
from django.urls import reverse
# Create your views here.

def showDemoPage(request):
    return render(request,"demo.html")

def showloginPage(request):
    return render(request,"login_page.html")
def dologin(request):
    if  request.method!="POST":
        return HttpResponseRedirect("<h2> method not allowed</h2")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("staff_home"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
        else:
            messages.error(request,"invalid login datails")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponseRedirect("user :"+request.user.email+" usertype: "+request.user.user_type)
    else:
        return HttpResponseRedirect("please login first")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")