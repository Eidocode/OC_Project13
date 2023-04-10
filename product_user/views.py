from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from product.models import DeviceUser, Device, Location
from product_user.forms import InventoryForm, ImmoForm, LocationForm, \
    ProductForm


@login_required
def show_last_users(request):
    """
    Used for product_user page
    """
    users = DeviceUser.objects.filter().order_by('-id')[:10]

    context = {
        'device_users': users
    }
    return render(request, 'device_users/last_device_users.html', context)


@login_required
def show_all_users(request):
    """
    Used for show_all_user page
    """
    users = DeviceUser.objects.filter().order_by('id')

    context = {
        'device_users': users
    }
    return render(request, 'device_users/device_users.html', context)


@login_required
def show_user_info(request, user_id):
    """
    Used for user_info page
    """

    # Gets a user designated by product_id or returns 404
    device_user = get_object_or_404(DeviceUser, pk=user_id)
    get_devices = Device.objects.filter(device_user_id=device_user.id)

    devices = []
    for item in get_devices:
        device_fullname = f"{item.product.brand.name} {item.product.name}"
        this_item = {
            'id': item.id,
            'type': item.product.category.name,
            'fullname': device_fullname,
        }
        devices.append(this_item)

    context = {
        'device_user': device_user,
        'devices': devices,
    }

    return render(request, 'device_users/device_users_info.html', context)


@login_required
def show_last_devices(request):
    """
    Used for product_device page
    """
    devices = Device.objects.filter().order_by('-id')[:10]

    context = {
        'devices': devices
    }
    return render(request, 'devices/last_devices.html', context)


@login_required
def show_all_devices(request):
    """
    Used for product_device page
    """
    devices = Device.objects.filter()

    context = {
        'devices': devices
    }
    return render(request, 'devices/all_devices.html', context)


@login_required
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


@login_required
def add_new_device(request):
    """
    Used for add_device page
    """
    product_form = ProductForm()
    inventory_form = InventoryForm()
    location_form = LocationForm()
    immo_form = ImmoForm()
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        inventory_form = InventoryForm(request.POST)
        location_form = LocationForm(request.POST)
        immo_form = ImmoForm(request.POST)
        if product_form.is_valid() and inventory_form.is_valid() and location_form.is_valid() and immo_form.is_valid():
            this_product = product_form.cleaned_data['name']
            this_inventory = inventory_form.save()
            this_location = location_form.cleaned_data['loc_name']

            this_immo = immo_form.save(commit=False)
            this_immo.location = Location.objects.get(pk=this_location.id)
            this_immo.save()

            new_device = Device(
                product_id=this_product.id,
                inventory_id=this_inventory.id,
                immo_id=this_immo.id,
            )
            new_device.save()

            print(f'{this_inventory.hostname} recorded to the database...')

            return redirect('show_all_devices')

    context = {
        'product_form': product_form,
        'inventory_form': inventory_form,
        'location_form': location_form,
        'immo_form': immo_form,
    }
    return render(request, 'devices/add_new_device.html', context)
