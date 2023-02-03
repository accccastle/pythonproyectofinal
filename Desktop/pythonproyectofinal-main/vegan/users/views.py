from django.shortcuts import render, redirect 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from users.forms import SignupForm, UpdateForm, UserProfileForm
from django.contrib.auth.models import User
from users.models import UserProfile
from django.views.generic import DeleteView

def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'users/login.html', context=context)
    
    elif request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'users/login_success.html')
            
        form = AuthenticationForm()
        context = {
            'form':form,
            'errors':'Usuario o contraseña incorrecto'
        }
        return render(request, 'users/login.html', context=context)
    
def login_success(request):
    return render(request, 'users/login_success.html', context={})

def signup(request):
    if request.method == 'GET':
        form = SignupForm()
        context = {
            'form':form
        } 
        return render(request, 'users/signup.html', context=context)
    
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('login')
        
        context = {
            'errors':form.errors,
            'form':SignupForm()
        }        
        return render(request, 'users/signup.html', context=context)
 
@login_required    
def update(request):
    user = request.user
    if request.method == 'GET':
        form = UpdateForm(initial = {
            'username':user.username,
            'first_name':user.first_name,
            'last_name':user.last_name
        })
        context = {
            'form':form
        } 
        return render(request, 'users/update.html', context=context)

    elif request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            return redirect('/') 
        
        context = {
            'errors':form.errors,
            'form':UpdateForm()
        }        
        return render(request, 'users/update.html', context=context)

@login_required    
def update_profile(request):
    user = request.user
    if request.method == 'GET':
        form = UserProfileForm(initial={
            'phone':request.user.profile.phone,
            'birth_date':request.user.profile.birth_date,
            'avatar':request.user.profile.avatar,
            'email':request.user.profile.email,
            'social_media':request.user.profile.social_media,
            'avatar':request.user.profile.avatar
        })
        context ={
            'form':form
        }
        return render(request, 'users/update_profile.html', context=context)

    elif request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            user.profile.birth_date = form.cleaned_data.get('birth_date')            
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.email = form.cleaned_data.get('email') 
            user.profile.social_media = form.cleaned_data.get('social_media')
            user.profile.avatar = form.cleaned_data.get('avatar')
            user.profile.save()
            return redirect('index')
        
        context = {
            'errors':form.errors,
            'form':UserProfileForm()
        }
        return render(request, 'users/register.html', context=context)  

class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = '/delete/'
    
def profile(request):
    return render(request, 'users/profile.html', context={})

