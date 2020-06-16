from django.http import HttpResponse
from django.shortcuts import render, redirect

from PIL import Image
from . import forms
from .process import hide_image, show_image

import os

def ocultar(request):
    form = forms.OcultaForm()
    if request.method == 'POST':
        form = forms.OcultaForm(request.POST, request.FILES)

        if form.is_valid():
            image_data = Image.open(request.FILES.get('image', False))
            image_file = hide_image.hide(image_data, form.cleaned_data['message'], form.cleaned_data['key'])

            if os.path.exists(image_file):
                with open(image_file, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/pdf")
                    response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(image_file)
                    return response

    context = {
        'ocultar': True,
        'form': form
    }
    return render(request, 'ocultar.html', context)

def revelar(request):
    form = forms.RevelaForm()
    context = {}
    if request.method == 'POST':
        form = forms.RevelaForm(request.POST, request.FILES)

        if form.is_valid():
            image_data = Image.open(request.FILES.get('image', False))
            message = show_image.show(image_data, form.cleaned_data['key'])
            context['message'] = message

    context['revelar'] = True,
    context['form'] = form
    return render(request, 'revelar.html', context)