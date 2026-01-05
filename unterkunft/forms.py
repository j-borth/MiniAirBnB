from django import forms
from .models import Unterkunft
from .models import Buchung

class BuchungForm(forms.ModelForm):
    class Meta:
        model = Buchung
        fields = ['startdatum', 'enddatum']
        widgets = {
            'startdatum': forms.DateInput(attrs={'type': 'date'}),
            'enddatum': forms.DateInput(attrs={'type': 'date'}),
        }
        
class UnterkunftForm(forms.ModelForm):
    class Meta:
        model = Unterkunft
        fields = ['titel', 'beschreibung', 'preis_pro_nacht']

