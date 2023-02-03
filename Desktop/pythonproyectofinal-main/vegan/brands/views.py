from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from brands.models import Brand
from brands.forms import BrandForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def create_brand(request):
    if request.method == 'GET':
        context = {
        'form': BrandForm()
    }

        return render(request,'brands/brand_create.html', context=context)

    elif request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            Brand.objects.create(
            name=form.cleaned_data['name'],
            type_brand=form.cleaned_data['type_brand'],
            web=form.cleaned_data['web'],
            image=form.cleaned_data['image'],
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
                'image': brand.image,
            }
        )
    }

        return render(request,'brands/brand_update.html', context=context)
    
    elif request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            brand.name=form.cleaned_data['name']
            brand.type_brand=form.cleaned_data['type_brand']
            brand.web=form.cleaned_data['web']
            brand.image=form.cleaned_data['image']
            brand.save()
            
        context = {
            'message': 'Actualizado! ✔'
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
    def get_queryset(self):
        queryset = super().get_queryset()
        search_fields = self.request.GET.get('search', '')
        if search_fields:
            queryset = queryset.filter(
                Q(name__icontains=search_fields) |
                Q(type_brand__icontains=search_fields) |
                Q(web__icontains=search_fields)
            )
        return queryset

class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'brands/brand_delete.html'
    success_url = '/delete/'
    
