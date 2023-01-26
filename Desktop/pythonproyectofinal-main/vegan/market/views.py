from django.shortcuts import render
from market.forms import MarketForm, LocationForm, RestoForm
from market.models import Market, Location, Restaurants
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView

@login_required
def create_market(request):
    if request.method == 'GET':
        context = {
            'form': MarketForm()
        }

        return render(request, 'market/market_formulario.html', context=context)

    elif request.method == 'POST':
        form = MarketForm(request.POST)
        if form.is_valid():
            Market.objects.create(
                name_market=form.cleaned_data['name_market'],
                name_product=form.cleaned_data['name_product'],
                price=form.cleaned_data['price'],
                location=form.cleaned_data['location'],
            )
            context = {
                'message': 'Producto creado exitosamente'
            }
            return render(request,'market/market_formulario.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': MarketForm()
            }
            return render(request,'market/market_formulario.html', context=context)

@login_required
def create_location(request):
        if request.method == 'GET':
            context = {
                'form': LocationForm()
            }

            return render(request, 'market/location_formulario.html', context=context)

        elif request.method == 'POST':
            form = LocationForm(request.POST)
            if form.is_valid():
                Location.objects.create(
                locationame=form.cleaned_data['locationame'],
                type_shop=form.cleaned_data['type_shop'],
                name_shop=form.cleaned_data['name_shop'],
            )
            context = {
                'message': 'Locacion creada exitosamente'
            }
            return render(request,'market/location_formulario.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': LocationForm()
            }
            return render(request,'market/location_formulario.html', context=context)

@login_required
def create_resto(request):
        if request.method == 'GET':
            context = {
                'form': RestoForm()
            }

            return render(request, 'market/resto_formulario.html', context=context)

        elif request.method == 'POST':
            form = RestoForm(request.POST)
            if form.is_valid():
                Restaurants.objects.create(
                name=form.cleaned_data['name'],
                location=form.cleaned_data['location'],
                food_type=form.cleaned_data['food_type'],
            )
            context = {
                'message': 'Restaurante creado exitosamente'
            }
            return render(request,'market/resto_formulario.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': RestoForm()
            }
            return render(request,'market/resto_formulario.html', context=context)

class MarketListView(ListView):
    model = Market
    template_name = 'market/market_list.html'
    ordering = ['name_market']

class LocationtListView(ListView):
    model = Location
    template_name = 'market/location_list.html'
    ordering = ['locationame']

class RestoListView(ListView):
    model = Restaurants
    template_name = 'market/resto_list.html'
    ordering = ['name']
    