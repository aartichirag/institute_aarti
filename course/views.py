from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import course_master
from django.http import JsonResponse

# Create your views here.
class NewCourse(CreateView):
    model = course_master
    fields = '__all__'

class ViewCourse(ListView):
    model = course_master
    context_object_name = 'courses'

class DetailCourse(DetailView):
    model = course_master

class UpdateCourse(UpdateView):
    model = course_master
    fields = '__all__'

class DeleteCourse(DeleteView):
    model = course_master
    success_url ='/course/view'

def get_fees(request, course_id):
        course = course_master.objects.get(pk=course_id);
        return JsonResponse({'fees': course.fees});

def get_course_chart_data(request):
    course=course_master.objects.all()
    label=[c.name for c in course]
    data=[c.duration for c in course]

    return JsonResponse({'data':data,'label':label})

def get_course_fees_chart_data(request):
    course=course_master.objects.all()
    label=[c.name for c in course]
    data=[c.fees for c in course]

    return JsonResponse({'data':data,'label':label})


