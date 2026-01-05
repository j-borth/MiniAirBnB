from django.urls import path
from . import views

urlpatterns = [
    # Nutzer-Perspektive
    path('', views.unterkunft_liste, name='unterkunft_liste'),
    path('<int:id>/', views.unterkunft_detail, name='unterkunft_detail'),

    # Anbieter-Perspektive
    path('anbieter/unterkuenfte/', views.anbieter_dashboard, name='anbieter_dashboard'),

    path('anbieter/unterkunft/neu/', views.unterkunft_erstellen, name='unterkunft_erstellen'),

    path('<int:id>/buchen/', views.buchung_erstellen, name='buchung_erstellen'),
]

