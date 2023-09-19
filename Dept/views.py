from django.shortcuts import render
from .models import Departments
# Create your views here.
def department(request):
      ab=Departments.objects.all()
      return render(request,'Department.html',{'z':ab})
