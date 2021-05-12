from django.shortcuts import render
from .models import inquiry_details
from django.views.generic import CreateView,ListView,UpdateView,DetailView

# Create your views here.
class NewInquiry(CreateView):
    model = inquiry_details
    fields = '__all__'

class ViewInquiry(ListView):
    model = inquiry_details
    context_object_name = 'inquiries'


class UpdateInquiry(UpdateView):
    model = inquiry_details
    fields = '__all__'

class DetailInquiry(DetailView):
    model = inquiry_details


