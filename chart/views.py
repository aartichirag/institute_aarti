from django.shortcuts import render
from course.models import course_master
from django.http import JsonResponse

# Create your views here.
def chartdemo(request):
    return render(request,"course/course_chart.html")

def get_chart(request):
    course_master.objects.all()




