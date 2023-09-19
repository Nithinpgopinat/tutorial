from django.shortcuts import render
from .models import Doctors
# Create your views here.
def Doctor(request):
      a=Doctors.objects.all()
      return render(request,'Doctors.html',{'z':a})