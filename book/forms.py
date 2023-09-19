from django import forms
from .models import Book

class DateInput(forms.DateInput):
    input_type='date'
    
class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = '__all__'
        
        widgets={
            'booking_date':DateInput(),
            }
        
        labels={
            'p_name':"Patient Name",
            'p_phone':"Phone Number",
            'p_email':"Email",
            'doc_name': "Doctor",
            
        }