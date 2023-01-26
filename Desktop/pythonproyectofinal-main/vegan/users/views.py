from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from users.forms import SignupForm

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
                context = {
                    'message':f'Bienvenido {username}'
                }
                return render(request, 'users/login_success.html', context=context)
            
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
            form.save()
            return redirect('login')
        
        context = {
            'errors':form.errors,
            'form':SignupForm()
        }
        
        return render(request, 'users/signup.html', context=context) 