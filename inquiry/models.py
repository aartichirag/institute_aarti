from django.db import models
from django.urls import reverse


# Create your models here.
class inquiry_details(models.Model):
    inquiry_date=models.DateField()
    first_name=models.CharField(max_length=30)
    second_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    st_name=models.CharField(max_length=30)
    area_name=models.CharField(max_length=30)
    city_name=models.CharField(max_length=30)
    mobile_number=models.CharField(max_length=11)
    phone_number_house=models.CharField(max_length=11)
    education=models.CharField(max_length=30)
    college_name=models.CharField(max_length=50)
    course=models.ManyToManyField('course.course_master',related_name="inquiry", blank=True)
    referance_name=models.CharField(max_length=50)
    remarks = models.CharField(max_length=20)
    inquiry_held_by=models.CharField(max_length=30)
    inquiry_institute_phone=models.CharField(max_length=11)
    demo_lecture_date=models.DateField(blank=True,null=True)
    demo_lecture_time=models.TimeField(blank=True,null=True)

    def __str__(self):
        return f"{self.id}-{self.first_name}"

    def get_absolute_url(self):
        return reverse('inquiry-view')


