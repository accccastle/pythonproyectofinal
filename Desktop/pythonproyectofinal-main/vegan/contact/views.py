from django.shortcuts import render
from contact.models import Contact
from contact.forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.mail import send_mail

@login_required
def contact(request):
    if request.method == 'GET':
        context = {
        'form': ContactForm()
    }

        return render(request,'contact.html', context=context)

    elif request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            Contact.objects.create(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            message=form.cleaned_data['message'],
            created=form.cleaned_data['created'],
        )
        context = {
            'message': 'Recibimos tu mensaje, te responderemos a la brevedad'
        }
        return render(request,'contact.html', context=context)
    else:
        context = {
            'form_errors': form.errors,
            'form': ContactForm()
        }
        return render(request,'contact.html', context=context)
    