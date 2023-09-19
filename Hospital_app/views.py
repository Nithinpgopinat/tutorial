from django.shortcuts import render
# from .forms import Feedback
# Create your views here.
def index(request):
    return render(request,'hospital.html')



def about(request):
    return render(request,'about_hospital.html')

def contact(request):
    
    return render(request,'contact_new.html')

  
