# services/forms.py

from django import forms
from .models import CleaningRequest

# This form lets users submit a new cleaning request
class CleaningRequestForm(forms.ModelForm):
    class Meta:
        model = CleaningRequest
        fields = ['customer_name', 'email', 'address', 'service_date', 'notes']
        widgets = {
            'service_date': forms.DateInput(attrs={'type': 'date'}),
        }
