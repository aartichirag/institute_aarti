from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator

# Create your models here.
class course_master(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    duration=models.IntegerField(validators=[MinValueValidator(0,"Duration should not be negative")])
    fees=models.IntegerField(validators=[MinValueValidator(0,"Fees should not be negative")])
    status=models.CharField(max_length=20, choices=[('Active','Active'),('Deactive', 'Deactive')])
    user=models.ForeignKey(User,on_delete=models.PROTECT,related_name='course')

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('course-view')