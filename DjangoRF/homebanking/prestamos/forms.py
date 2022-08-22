from locale import format_string
from django import forms
from datetime import timezone
from .models import Prestamo


class PrestamosForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['loan_type', 'loan_total']
