from django.shortcuts import render

from product.models import Device


def dashboard(request):
    devices_qs = Device.objects.filter()

    context = {
        'devices_qs': devices_qs,
    }

    return render(request, 'dashboard/dashboard.html', context)
