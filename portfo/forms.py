from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'text-red-400'}),
            'email': forms.EmailInput(attrs={'class': 'text-red-400'}),
            'phone_number': forms.NumberInput(attrs={'class': 'text-red-400'}),
            'message': forms.Textarea(attrs={'class': 'text-red-400'}),
        }
