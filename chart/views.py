from django.shortcuts import render



# Create your views here.
def chartdemo(request):
    return render(request,"course/course_chart.html")