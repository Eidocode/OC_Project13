from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from product.models import Device, Category


def dashboard(request, device_type=None):
    devices_qs = Device.objects.all()
    categories_qs = Category.objects.all()

    if device_type == 'All devices':
        data = [{'name': device.inventory.hostname} for device in devices_qs]
        return JsonResponse(data, safe=False)

    if device_type:
        category = get_object_or_404(Category, name=device_type)
        devices = Device.objects.filter(product__category=category)
        data = [{'name': device.inventory.hostname} for device in devices]
        return JsonResponse(data, safe=False)

    context = {
        'devices': devices_qs,
        'categories': categories_qs,
    }

    if request.is_ajax():
        return JsonResponse(context)

    return render(request, 'dashboard/dashboard.html', context)


# def device_list(request, device_type=None):
#     if device_type:
#         category = get_object_or_404(Category, name=device_type)
#         devices = Device.objects.filter(product__category=category)
#         data = [{'name': device.inventory.hostname} for device in devices]
#         return JsonResponse(data, safe=False)
#
#     devices_qs = Device.objects.all()
#     categories_qs = Category.objects.all()
#
#     context = {
#         'devices': devices_qs,
#         'categories': categories_qs,
#     }
#
#     return render(request, 'dashboard/device_list.html', context)
