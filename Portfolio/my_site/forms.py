from django import forms
from django.core.exceptions import ValidationError
from .models import FeedBack


class FeedbackForms(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['name', 'email', 'feedback']