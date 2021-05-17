from django.db import models
from django.urls import reverse
from addmission.models import addmission_details
from django.core.validators import FileExtensionValidator

# Create your models here.
class certificate(models.Model):
    date=models.DateField()
    addmission=models.ForeignKey(addmission_details,on_delete=models.CASCADE,related_name="certificate")
    photo=models.ImageField(upload_to='images', blank=True,validators=[FileExtensionValidator(['jpg','png','jpeg'],"File extension is invalid")])

    def __str__(self):
        return f"{self.addmission}"

    def get_absolute_url(self):
        return reverse('certifiacate-view')
