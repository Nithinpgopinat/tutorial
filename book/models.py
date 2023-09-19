from django.db import models
from Doct.models import Doctors
# Create your models here.
class Book(models.Model):
    p_name=models.CharField(max_length=100)
    p_phone=models.CharField(max_length=100)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.doc_name
    