from django.db import models

# Create your models here.
class Doctors(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_spec=models.CharField(max_length=255)
    dep_name=models.CharField(max_length=255)
    doc_image=models.ImageField(upload_to='pics')
    
    def __str__(self):
        return self.doc_name