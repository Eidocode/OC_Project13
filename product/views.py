from django.shortcuts import render

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
