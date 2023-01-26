from django import forms

class BrandForm(forms.Form):
    TYPE_CHOICES = (
    ('Supermercado','Supermercado'),
    ('Restaurante','Restaurante'),
    ('Emprendimiento','Emprendimiento'),
    )
    name = forms.CharField(max_length=50, label='Nombre')
    type_brand = forms.ChoiceField(choices=TYPE_CHOICES, label='Tipo de Marca')
    web = forms.URLField(max_length=200)