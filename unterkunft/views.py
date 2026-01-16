from .forms import UnterkunftForm, BuchungForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Unterkunft, Buchung
from django.contrib.auth.decorators import login_required


def unterkunft_liste(request):
    unterkuenfte = Unterkunft.objects.all()
    return render(request, 'unterkunft/unterkunft_liste.html', {'unterkuenfte': unterkuenfte})


def unterkunft_detail(request, id):
    unterkunft = get_object_or_404(Unterkunft, id=id)
    return render(request, 'unterkunft/unterkunft_detail.html', {'unterkunft': unterkunft})


@login_required
def anbieter_dashboard(request):
    unterkuenfte = Unterkunft.objects.filter(anbieter=request.user)
    return render(request, 'unterkunft/anbieter_dashboard.html', {
        'unterkuenfte': unterkuenfte
    })
@login_required
def unterkunft_erstellen(request):
    if request.method == 'POST':
        form = UnterkunftForm(request.POST)
        if form.is_valid():
            unterkunft = form.save(commit=False)
            unterkunft.anbieter = request.user  
            unterkunft.save()
            return redirect('anbieter_dashboard')
    else:
        form = UnterkunftForm()
    return render(request, 'unterkunft/unterkunft_form.html', {'form': form})

@login_required
def buchung_erstellen(request, id):
    unterkunft = get_object_or_404(Unterkunft, id=id)
    if request.method == 'POST':
        form = BuchungForm(request.POST)
        if form.is_valid():
            buchung = form.save(commit=False)
            buchung.unterkunft = unterkunft
            buchung.nutzer = request.user 
            buchung.save()
            return redirect('unterkunft_liste')
    else:
        form = BuchungForm()
    return render(request, 'unterkunft/buchung_form.html', {
        'form': form,
        'unterkunft': unterkunft})

@login_required
def anbieter_dashboard(request):
    meine_unterkuenfte = Unterkunft.objects.filter(anbieter=request.user)
    
    meine_buchungen = Buchung.objects.filter(unterkunft__anbieter=request.user)
    
    return render(request, 'unterkunft/anbieter_dashboard.html', {
        'unterkuenfte': meine_unterkuenfte,
        'buchungen': meine_buchungen
    })