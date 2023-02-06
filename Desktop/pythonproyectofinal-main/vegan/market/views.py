from django.shortcuts import render
from market.forms import MarketForm, LocationForm, RestoForm
from market.models import Market, Location, Restaurants
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import PermissionRequiredMixin

@login_required
def create_market(request):
    if request.method == 'GET':
        context = {
            'form': MarketForm()
        }

        return render(request, 'market/market_formulario.html', context=context)

    elif request.method == 'POST':
        form = MarketForm(request.POST, request.FILES)
        if form.is_valid():
            Market.objects.create(
                name_market=form.cleaned_data['name_market'],
                name_product=form.cleaned_data['name_product'],
                price=form.cleaned_data['price'],
                location=form.cleaned_data['location'],
                image_product=form.cleaned_data['image_product'],
                notes=form.cleaned_data['notes'],
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
def update_market(request, pk):
    market = Market.objects.get(id=pk)
    if request.method == 'GET':
        context = {
        'form': MarketForm(
            initial={
                'name_market': market.name_market,
                'name_product': market.name_product,
                'location': market.location,
                'price': market.price,
                'image_product': market.image_product,
                'notes': market.notes,
            }
        )
    }

        return render(request,'market/market_update.html', context=context)
    
    elif request.method == 'POST':
        form = MarketForm(request.POST, request.FILES)
        if form.is_valid():
            market.name_market=form.cleaned_data['name_market']
            market.name_product=form.cleaned_data['name_product']
            market.location=form.cleaned_data['location']
            market.price=form.cleaned_data['price']
            market.image_product=form.cleaned_data['image_product']
            market.notes=form.cleaned_data['notes']
            market.save()
            
        context = {
            'message': 'Actualizado! ✔'
        }
        return render(request,'market/market_update.html', context=context)
    else:
        context = {
            'form_errors': form.errors,
            'form': MarketForm()
        }
    return render(request,'market/market_update.html', context=context)

class MarketListView(ListView):
    model = Market
    template_name = 'market/market_list.html'
    ordering = ['name_market']
    def get_queryset(self):
        queryset = super().get_queryset()
        search_fields = self.request.GET.get('search', '')
        if search_fields:
            queryset = queryset.filter(
                Q(name_market__icontains=search_fields) |
                Q(name_product__icontains=search_fields) |
                Q(location__icontains=search_fields)     |
                Q(notes__icontains=search_fields)   
            )
        return queryset

class MarketDeleteView(DeleteView, PermissionRequiredMixin):
    model = Market
    template_name = 'market/market_delete.html'
    success_url = '/delete/'

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
                'message': 'Creado exitosamente'
            }
            return render(request,'market/location_formulario.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': LocationForm()
            }
            return render(request,'market/location_formulario.html', context=context)

@login_required
def update_location(request, pk):
    location = Location.objects.get(id=pk)
    if request.method == 'GET':
        context = {
        'form': LocationForm(
            initial={
                'name_market': location.locationame,
                'type_shop': location.type_shop,
                'name_shop': location.name_shop,
            }
        )
    }

        return render(request,'market/location_update.html', context=context)
    
    elif request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location.locationame=form.cleaned_data['locationame']
            location.type_shop=form.cleaned_data['type_shop']
            location.name_shop=form.cleaned_data['name_shop']
            location.save()
            
        context = {
            'message': 'Actualizado! ✔'
        }
        return render(request,'market/location_update.html', context=context)
    else:
        context = {
            'form_errors': form.errors,
            'form': MarketForm()
        }
        return render(request,'market/location_update.html', context=context) 

class LocationtListView(ListView):
    model = Location
    template_name = 'market/location_list.html'
    ordering = ['locationame']
    def get_queryset(self):
        queryset = super().get_queryset()
        search_fields = self.request.GET.get('search', '')
        if search_fields:
            queryset = queryset.filter(
                Q(locationame__icontains=search_fields) |
                Q(type_shop__icontains=search_fields) |
                Q(name_shop__icontains=search_fields)
            )
        return queryset

class LocationDeleteView(DeleteView, PermissionRequiredMixin):
    model = Location
    template_name = 'market/location_delete.html'
    success_url = '/delete/'

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
                'message': 'Creado exitosamente'
            }
            return render(request,'market/resto_formulario.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': RestoForm()
            }
            return render(request,'market/resto_formulario.html', context=context)

@login_required
def update_resto(request, pk):
    resto = Restaurants.objects.get(id=pk)
    if request.method == 'GET':
        context = {
        'form': RestoForm(
            initial={
                'name': resto.name,
                'location': resto.location,
                'food_type': resto.food_type,
            }
        )
    }

        return render(request,'market/resto_update.html', context=context)
    
    elif request.method == 'POST':
        form = RestoForm(request.POST)
        if form.is_valid():
            resto.name=form.cleaned_data['name']
            resto.location=form.cleaned_data['location']
            resto.food_type=form.cleaned_data['food_type']
            resto.save()
            
        context = {
            'message': 'Actualizado! ✔'
        }
        return render(request,'market/resto_update.html', context=context)
    else:
        context = {
            'form_errors': form.errors,
            'form': RestoForm()
        }
        return render(request,'market/resto_update.html', context=context) 

class RestoListView(ListView):
    model = Restaurants
    template_name = 'market/resto_list.html'
    ordering = ['name']
    def get_queryset(self):
        queryset = super().get_queryset()
        search_fields = self.request.GET.get('search', '')
        if search_fields:
            queryset = queryset.filter(
                Q(name__icontains=search_fields) |
                Q(location__icontains=search_fields) |
                Q(food_type__icontains=search_fields)
            )
        return queryset
 
class RestoDeleteView(DeleteView, PermissionRequiredMixin):
    model = Restaurants
    template_name = 'market/resto_delete.html'
    success_url = '/delete/'

