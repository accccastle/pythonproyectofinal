from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from brands.models import Brand
from brands.forms import BrandForm
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
def create_brand(request):
    if request.method == 'GET':
        context = {
        'form': BrandForm()
    }

        return render(request,'brands/brand_create.html', context=context)

    elif request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            Brand.objects.create(
            name=form.cleaned_data['name'],
            type_brand=form.cleaned_data['type_brand'],
            web=form.cleaned_data['web'],
        )
        context = {
            'message': 'Marca Creada! :)'
        }
        return render(request,'brands/brand_create.html', context=context)
    else:
        context = {
            'form_errors': form.errors,
            'form': BrandForm()
        }
        return render(request,'brands/brand_create.html', context=context)

@login_required
def update_brand(request, pk):
    brand = Brand.objects.get(id=pk)
    if request.method == 'GET':
        context = {
        'form': BrandForm(
            initial={
                'name': brand.name,
                'type_brand': brand.type_brand,
                'web': brand.web,
            }
        )
    }

        return render(request,'brands/brand_update.html', context=context)
    
    elif request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand.name=form.cleaned_data['name']
            brand.type_brand=form.cleaned_data['type_brand']
            brand.web=form.cleaned_data['web']
            brand.save()
            
        context = {
            'message': 'Actualizado! :)'
        }
        return render(request,'brands/brand_update.html', context=context)
    else:
        context = {
            'form_errors': form.errors,
            'form': BrandForm()
        }
        return render(request,'brands/brand_update.html', context=context)
    
class BrandsListView(ListView):
    model = Brand
    template_name = 'brands/brand_list.html'
    queryset = Brand.objects.filter(is_active = True)
    ordering = ['name']

class BrandDeleteView(LoginRequiredMixin, DeleteView):
    model = Brand
    template_name = 'brands/brand_delete.html'
    success_url = '/brands/brand-list/'