from django.shortcuts import render, get_object_or_404, redirect

from product.models import DeviceUser, Device
from product_user.forms import AddDeviceForm


def show_last_users(request):
    """
    Used for product_user page
    """
    users = DeviceUser.objects.filter().order_by('-id')[:10]

    context = {
        'device_users': users
    }
    return render(request, 'device_users/last_device_users.html', context)


def show_all_users(request):
    """
    Used for show_all_user page
    """
    users = DeviceUser.objects.filter().order_by('id')

    context = {
        'device_users': users
    }
    return render(request, 'device_users/device_users.html', context)


def show_user_info(request, user_id):
    """
    Used for user_info page
    """

    # Gets a user designated by product_id or returns 404
    user = get_object_or_404(DeviceUser, pk=user_id)
    get_devices = Device.objects.filter(device_user_id=user.id)

    devices = []
    for item in get_devices:
        device_fullname = f"{item.product.brand.name} {item.product.name}"
        this_item = {
            'id': item.id,
            'fullname': device_fullname,
        }
        devices.append(this_item)

    context = {
        'user': user,
        'devices': devices,
    }

    return render(request, 'device_users/device_users_info.html', context)


def show_last_devices(request):
    """
    Used for product_device page
    """
    devices = Device.objects.filter().order_by('-id')[:10]

    context = {
        'devices': devices
    }
    return render(request, 'devices/last_devices.html', context)


def show_all_devices(request):
    """
    Used for product_device page
    """
    devices = Device.objects.filter()

    context = {
        'devices': devices
    }
    return render(request, 'devices/all_devices.html', context)


def show_device_info(request, device_id):
    """
    Used for device_info page
    """

    # Gets a device designated by product_id or returns 404
    device = get_object_or_404(Device, pk=device_id)

    context = {
        'device': device,
    }
    return render(request, 'devices/device_info.html', context)


def add_device(request):
    """
    Used for add_device page
    """
    form = AddDeviceForm()
    if request.method == 'POST':
        form = AddDeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_all_devices')

    return render(request, 'devices/add_device.html', {'form': form})
