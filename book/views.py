from django.shortcuts import render,redirect
# from .models import Booking
from .forms import BookingForm
# Create your views here.
def Booking(request):
      if request.method=="POST":
       form=BookingForm(request.POST)
       if form.is_valid():
             form.save()
             return redirect("/")
      form=BookingForm()
     
      dict_form={
      'form':form}
      return render(request,'booking.html',dict_form)