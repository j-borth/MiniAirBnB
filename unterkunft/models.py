from django.db import models
from django.contrib.auth.models import User

class Unterkunft(models.Model):
    titel = models.CharField(max_length=100)
    beschreibung = models.TextField()
    preis_pro_nacht = models.FloatField()

    anbieter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='unterkuenfte', null=True)
    
    class Meta:
        verbose_name = 'Unterkunft'
        verbose_name_plural = 'Unterkünfte'

    def __str__(self):
        return self.titel 

from django.db import models
from django.contrib.auth.models import User

class Buchung(models.Model):
    unterkunft = models.ForeignKey('Unterkunft', on_delete=models.CASCADE)
    nutzer = models.ForeignKey(User, on_delete=models.CASCADE)
    startdatum = models.DateField()
    enddatum = models.DateField()
    erstellt_am = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Buchung'
        verbose_name_plural = 'Buchungen'

    STATUS_CHOICES = [
        ('offen', 'Offen'),
        ('bestätigt', 'Bestätigt'),
        ('abgesagt', 'Abgesagt'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='offen')

    def __str__(self):
        return f"Buchung von {self.nutzer} für {self.unterkunft} ({self.startdatum} – {self.enddatum})"

        