from django import forms


class OcultaForm(forms.Form):
    image = forms.ImageField(
        label='Imagen:',
        required=False,
        help_text='''
            Esta sera la imagen en la 
            que se oculte el mensaje.
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
        max_length=500,
        required=False,
        widget=forms.Textarea(
            attrs={'rows': 3, 'class': 'form-control'}),
        help_text='''
            En caso de que el mensaje no pueda ser 
            cubierto por la imagen, se truncara.
        ''')
    