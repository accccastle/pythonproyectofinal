from django import forms

class MarketForm(forms.Form):
    name_market = forms.CharField(label='Mercado', max_length=100, required=False)
    name_product = forms.CharField(label='Producto', max_length=100, required=False)
    location = forms.CharField(label='Ubicacion', max_length=100, required=False)
    price = forms.FloatField(label='Precio', required=False)
    image_product = forms.ImageField(label='Imagen del Producto')
    notes = forms.CharField(label='Notas', max_length=1000, required=False)
    
    
class RestoForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    location = forms.CharField(label='Ubicacion', max_length=100)
    food_type = forms.CharField(label='Tipo de Comida', max_length=100)
    
class LocationForm(forms.Form):
    locationame = forms.CharField(label='Ubicacion', max_length=100)
    type_shop = forms.CharField(label='Tipo', max_length=100)
    name_shop = forms.CharField(label='Nombre', max_length=100)   