from django.contrib import admin
from .models import Unterkunft, Buchung


@admin.register(Unterkunft)
class UnterkunftAdmin(admin.ModelAdmin):
    list_display = ('titel', 'preis_pro_nacht', 'anbieter')
    list_filter = ('anbieter',)
    search_fields = ('titel',)


@admin.register(Buchung)
class BuchungAdmin(admin.ModelAdmin):
    list_display = ('unterkunft', 'nutzer', 'startdatum', 'enddatum', 'status')
    list_filter = ('status',)


