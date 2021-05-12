from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.
class addmission_details(models.Model):
    student=models.ForeignKey('student.student_personal_info',on_delete=models.CASCADE, related_name="addmissions")
    date_of_addmission=models.DateField(default=datetime.utcnow)
    course=models.OneToOneField('course.course_master',on_delete=models.CASCADE,related_name="addmissions")
    start_time=models.TimeField()
    end_time=models.TimeField()
    start_date=models.DateField()
    end_date=models.DateField()
    scan_copy_of_id_proof=models.FileField(upload_to='documents')
    fees=models.IntegerField()
    status=models.CharField(max_length=10,choices=[('Active','Active'),('On hold','On hold'),('Close','Close')])
    no_of_days=models.IntegerField()
    remarks=models.CharField(max_length=20)
    pending_fees=models.IntegerField()
    inquiry=models.ForeignKey('inquiry.inquiry_details',default=4,on_delete=models.CASCADE,related_name="addmission")

    def __str__(self):
        return f"{self.id}-{self.student}-{self.course}"

    def get_absolute_url(self):
        return reverse('addmission-view')

