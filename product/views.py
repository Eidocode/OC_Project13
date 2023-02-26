from django.contrib import messages
from django.shortcuts import render

from product.forms import ContactUsForm
from product.models import Device


def index(request):
    """
    Used for index page
    """
    devices = Device.objects.filter().order_by('-added_date')[:5]
    current_user = request.user

    context = {
        'devices': devices
    }
    return render(request, 'product/index.html', context)


def contact_us(request):
    """
    Used for contact us page
    """
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            messages.success(request, f'Bonjour {form.cleaned_data["first_name"]}! Merci pour votre message...')

    context = {
        'form': form,
    }
    return render(request, 'product/contact_us.html', context)
