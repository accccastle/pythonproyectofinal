from django import forms

class BrandForm(forms.Form):
    TYPE_CHOICES = (
    ('Mercado','Mercado'),
    ('Restaurante','Restaurante'),
    ('Emprendimiento','Emprendimiento'),
    )
    name = forms.CharField(max_length=50, label='Nombre', required=False)
    type_brand = forms.ChoiceField(choices=TYPE_CHOICES, label='Tipo de Marca', required=False)
    web = forms.URLField(max_length=200, required=False, label='Sitio Web')
    image = forms.ImageField(label='Imagen de la Marca', required=False)
