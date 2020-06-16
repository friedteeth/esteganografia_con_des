from django.shortcuts import render
from PIL import Image
from . import forms
from .process import hide_image

def ocultar(request):
    form = forms.OcultaForm()
    if request.method == 'POST':
        form = forms.OcultaForm(request.POST)
        image = request.FILES.get('image', False)

        if form.is_valid() and image:
            image_data = Image.open(image)
            hide_image.hide(image_data, form.cleaned_data['message'], form.cleaned_data['key'])

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