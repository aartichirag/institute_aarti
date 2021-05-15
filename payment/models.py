from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator

# Create your models here.
class payment_details(models.Model):
    receipt_date=models.DateField()
    amount=models.IntegerField(validators=[MinValueValidator(0,"Amount should not be negative")])
    type=models.CharField(max_length=10, choices=[('Cash','Cash'),('Chaque', 'Chaque')])
    chaque_no=models.CharField(blank=True,null=True,max_length=30)
    bank_name=models.CharField(max_length=30,blank=True,null=True)
    branch_name=models.CharField(max_length=30,blank=True,null=True)
    chaque_date=models.DateField(blank=True, null=True)
    addmission=models.ForeignKey('addmission.addmission_details',default=2,on_delete=models.CASCADE,related_name="payment")

    def __str__(self):
        return f"{self.receipt}-{self.type}-{self.bank_name}"

    def get_absolute_url(self):
        return reverse('payment-view')
