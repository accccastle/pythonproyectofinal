from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='Nombre', required=False)
    email = forms.EmailField(label='Correo Electrónico', required=False)
    message = forms.Textarea()
    created = forms.DateField(label='Fecha de Creación', required=False)
    