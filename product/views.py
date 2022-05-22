from django.shortcuts import render

from product.models import Device


def index(request):
    """
    Used for index page
    """
    devices = Device.objects.all()

    context = {
        'devices': devices
    }
    return render(request, 'product/index.html', context)
