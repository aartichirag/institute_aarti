from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import addmission_details


# Create your views here.
class NewAddmission(CreateView):
    model = addmission_details
    fields = '__all__'

class ViewAddmission(ListView):
    model = addmission_details
    context_object_name = 'addmissions'

class UpdateAddmission(UpdateView):
    model = addmission_details
    fields = '__all__'

class DetailAddmission(DetailView):
    model = addmission_details

class DeleteAddmission(DeleteView):
    model = addmission_details
    success_url = '/addmission/view'


