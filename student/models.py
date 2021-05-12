from django.db import models
from django.urls import reverse


# Create your models here.
class student_personal_info(models.Model):
    student_first_name=models.CharField(max_length=30)
    student_last_name=models.CharField(max_length=30)
    student_second_name=models.CharField(max_length=30)
    father_first_name=models.CharField(max_length=30)
    father_second_name=models.CharField(max_length=30)
    father_last_name=models.CharField(max_length=30)
    houseno_building_name=models.TextField()
    st_name=models.CharField(max_length=30)
    area_name=models.CharField(max_length=30)
    city_name=models.CharField(max_length=30)
    country_name=models.CharField(max_length=30)
    mobile_number=models.CharField(max_length=11)
    phone_number_house=models.CharField(max_length=11)
    birthdate=models.DateField()
    gender=models.CharField(max_length=10,choices=[('Male','Male'),('Female','Female')])
    school_college_name=models.CharField(max_length=50)
    education=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='images')
    biomatric_data=models.CharField(max_length=30)
    email_id=models.CharField(max_length=30)
    inquiry_id=models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.student_first_name}"

    def get_absolute_url(self):
        return reverse('student-view')


