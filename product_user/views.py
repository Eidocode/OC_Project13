from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect

from product.models import DeviceUser, Device
from product_user.forms import InventoryForm, ImmoForm, LocationForm, \
    ProductForm


@login_required
def show_last_users(request):
    """
    View for DeviceUser page (last users)
    """
    # Gets the 10 last DeviceUser objects
    users = DeviceUser.objects.select_related(
        'assignment', 'status').order_by('-id')[:10]
    context = {
        'device_users': users
    }
    return render(request, 'device_users/last_device_users.html', context)


@login_required
def show_all_users(request):
    """
    View for DeviceUser page (All users)
    """
    # Gets all DeviceUser objects
    users = DeviceUser.objects.select_related(
        'assignment', 'status').order_by('-id')
    context = {
        'device_users': users
    }
    return render(request, 'device_users/device_users.html', context)


@login_required
def show_user_info(request, user_id):
    """
    View for DeviceUser information page
    """
    # Gets a DeviceUser object designated by user_id or returns 404
    device_user = get_object_or_404(DeviceUser, pk=user_id)
    # Gets all DeviceUser objects designated by device_user_id
    get_devices = Device.objects.filter(device_user_id=device_user.id)

    devices = []
    # Formats the information far each Device object
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
    View for Devices page (last devices)
    """
    # Gets the 10 last Device objects
    devices = Device.objects.select_related(
        'product__category', 'product__brand', 'product', 'device_user',
        'inventory', 'immo', 'immo__location__site').order_by('-id')[:10]
    context = {
        'devices': devices
    }
    return render(request, 'devices/last_devices.html', context)


@login_required
def show_all_devices(request):
    """
    View for Devices page (all devices)
    """
    # Gets all Device objects
    devices = Device.objects.select_related(
        'product__category', 'product__brand', 'product', 'device_user',
        'inventory', 'immo', 'immo__location__site').order_by('-id')
    context = {
        'devices': devices
    }
    return render(request, 'devices/all_devices.html', context)


@login_required
def show_device_info(request, device_id):
    """
    View for Device information page
    """
    # Gets a device object designated by device_id or returns 404
    device = get_object_or_404(Device, pk=device_id)
    context = {
        'device': device,
    }
    return render(request, 'devices/device_info.html', context)


@login_required
def add_new_device(request):
    """
    View for add new Device page
    """
    # Sets instances of the forms needed for adding a new device
    product_form = ProductForm()
    inventory_form = InventoryForm()
    location_form = LocationForm()
    immo_form = ImmoForm()

    if request.method == 'POST':
        # Filling the forms with the data sent by the user
        product_form = ProductForm(request.POST)
        inventory_form = InventoryForm(request.POST)
        location_form = LocationForm(request.POST)
        immo_form = ImmoForm(request.POST)

        # Checks if the forms are valid
        if product_form.is_valid() and inventory_form.is_valid() and \
                location_form.is_valid() and immo_form.is_valid():
            # Gets the product name
            this_product = product_form.cleaned_data['name']
            # Gets the location name
            this_location = location_form.cleaned_data['loc_name']

            # Creates a transaction for saving the new device
            with transaction.atomic():
                # Saves the inventory form data
                this_inventory = inventory_form.save()
                # Saves the immo form data but not commiting to the database
                this_immo = immo_form.save(commit=False)
                # Sets the location of the immo and saves to the database
                this_immo.location = this_location
                this_immo.save()

                # Saves the device to the database
                new_device = Device(
                    product=this_product,
                    inventory=this_inventory,
                    immo=this_immo,
                )
                new_device.save()
                print(f'{this_inventory.hostname} recorded to the database...')

            # Redirects to the show_all_devices page after successful saving
            return redirect('show_all_devices')

    context = {
        'product_form': product_form,
        'inventory_form': inventory_form,
        'location_form': location_form,
        'immo_form': immo_form,
    }
    return render(request, 'devices/add_new_device.html', context)
