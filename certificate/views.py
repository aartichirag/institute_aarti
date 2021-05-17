from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import certificate

# Create your views here.
class NewCertificate(CreateView):
    model = certificate
    fields = '__all__'

class ViewCertificate(ListView):
    model = certificate
    context_object_name = 'certificates'

class UpdateCertificate(UpdateView):
    model = certificate
    fields = '__all__'

class DeleteCertificate(DeleteView):
    model = certificate
    success_url = '/certificate/view'