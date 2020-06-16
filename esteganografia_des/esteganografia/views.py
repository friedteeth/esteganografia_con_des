from django.shortcuts import render
from . import forms

def ocultar(request):
    form = forms.OcultaForm()
    if request.method == 'POST':
        form = forms.OcultaForm(request.POST)
        files = request.FILES

        if form.is_valid() and files.get('image', False):
            
        else:
            print('no es valido')
    context = {
        'ocultar': True,
        'form': form
    }
    return render(request, 'ocultar.html', context)

def revelar(request):
    context = {
        'revelar': True
    }
    return render(request, 'revelar.html', context)