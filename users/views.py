from django.shortcuts import render
from student.models import student_personal_info
from course.models import course_master
from addmission.models import addmission_details
from payment.models import payment_details
from inquiry.models import inquiry_details
# Create your views here.
def home(request):
    return render(request,"users/home.html",{
        "studcount":student_personal_info.objects.count(),
        "coursecount":course_master.objects.count(),
        "addmissioncount":addmission_details.objects.count(),
        "paymentcount":payment_details.objects.count(),
        "inquirycount":inquiry_details.objects.count()
    })