from django import forms
from django.core.validators import FileExtensionValidator
from PIL import Image


class OcultaForm(forms.Form):
    image = forms.ImageField(
        label='Imagen:',
        required=False,
        # validators=[FileExtensionValidator(allowed_extensions=['png'])],
        help_text='''
            Esta sera la imagen en la 
            que se oculte el mensaje. NOTA 
            unicamente se aceptan imagenes 
            con formatos png.
        ''')
    key = forms.CharField(
        label="Llave",
        max_length=8,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
        help_text='''
            Para el cifrado DES la llave debe de 
            tener una longitud de 64 bits o 8 
            caracteres.
        ''')
    message = forms.CharField(
        label="Mensaje:",
        required=False,
        widget=forms.Textarea(
            attrs={'rows': 3, 'class': 'form-control'}),
        help_text='''
            En caso de que el mensaje no pueda ser 
            cubierto por la imagen, se truncara.
            Nota es posible que esto conlleve a que 
            el mensaje decodificado muestre caracteres
            inlegibles.
        ''')
    
    # def clean_image(self):
    #     image = self.cleaned_data["image"]
    #     pillow_image = Image.open(image)

    #     if pillow_image.format.lower() != 'png':
    #         raise forms.ValidationError("Formato de imagen no soportado. El unico formato soportado es PNG.")

    #     return image

class RevelaForm(forms.Form):
    image = forms.ImageField(
        label='Imagen:',
        required=False,
        # validators=[FileExtensionValidator(allowed_extensions=['png'])],
        help_text='''
            Esta sera la imagen en la 
            que se buscara un mensaje.
        ''')
    key = forms.CharField(
        label="Llave",
        max_length=8,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
        help_text='''
            Para el cifrado DES la llave debe de 
            tener una longitud de 64 bits o 8 
            caracteres.
        ''')
    