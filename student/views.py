from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import student_personal_info

# Create your views here.
class NewStudent(CreateView):
    model = student_personal_info
    fields = '__all__'

class ViewStudent(ListView):
    model = student_personal_info
    context_object_name = 'students'

class UpdateStudent(UpdateView):
    model = student_personal_info
    fields = '__all__'

class DeleteStudent(DeleteView):
    model = student_personal_info
    success_url = '/student/view'

class StudentDetail(DetailView):
    model = student_personal_info