from django import forms
from .models import Customer
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_email', 'customer_phone', 'customer_address']  # Match exactly with model field names
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter customer name'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'customer_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter address', 'rows': 1}),
        }
