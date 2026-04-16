from django import forms
from .models import Job, Resource, ContactMessage


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'category', 'description', 'location', 'deadline', 'apply_link', 'is_active']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'category', 'file', 'external_link', 'thumbnail', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'subject': forms.TextInput(attrs={'placeholder': 'How can we help you?'}),
            'message': forms.Textarea(attrs={
                'rows': 6,
                'placeholder': 'Write your message here...'
            }),
        }