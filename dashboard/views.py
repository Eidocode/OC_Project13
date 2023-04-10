import calendar
from collections import OrderedDict

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from dashboard.forms import SearchForm
from product.models import Device, Category, Brand, Entity, OperatingSystem


def get_devices_by_brand(queryset_brands, queryset_devices):
    """
    Returns a dict with the brands of all devices in queryset_devices and the
    number of matching devices for each brand.
    """
    devices_by_brand = {}
    for brand in queryset_brands:
        # Count the number of devices for each brand
        filtered_devices = queryset_devices.filter(product__brand=brand).count()
        # Add an entry to the dict with the brand name and the number of devices
        devices_by_brand[brand.name] = filtered_devices
    return devices_by_brand


def get_devices_by_entities(queryset_entities, queryset_devices):
    """
    Returns a dict with the entities in queryset_devices, and the number of
    devices for each entity.
    """
    devices_by_entities = {}
    for entity in queryset_entities:
        # Count the number of devices for each entity
        filtered_devices = queryset_devices.filter(immo__location__site=entity).count()
        # Add an entry to the dict with entity name and the number of devices
        devices_by_entities[entity.name] = filtered_devices
    return devices_by_entities


def get_devices_by_os(queryset_devices):
    """
    Returns a dict with the OS of all devices in queryset_devices and the
    number of matching devices for each OS.
    """
    devices_by_os = {}
    for os in OperatingSystem.objects.all():
        # Count the number of devices for each OS
        filtered_devices = queryset_devices.filter(
            inventory__operating_system__name=os).count()
        # Add an entry to the dict with the OS name and the number of devices
        devices_by_os[os.name] = filtered_devices
    return devices_by_os


def count_devices_by_month(queryset_devices, year):
    """
    Returns a dict with the number of devices added each month in the specified year
    """
    months_count = {}
    filtered_qs = queryset_devices.filter(added_date__year=year)
    for device in filtered_qs:
        # Get the device added date
        this_date = device.added_date
        # Get the month in "mmm" format (ex: "Jan")
        month = this_date.strftime("%b")
        # If month already exists, the counter is incremented by 1
        if month in months_count:
            months_count[month] += 1
        # else, we add a new entry with a counter set to 1
        else:
            months_count[month] = 1
    sorted_months_count = OrderedDict()
    for month_number in range(1, 13):
        month_name = calendar.month_name[month_number][:3]
        sorted_months_count[month_name] = months_count.get(month_name, 0)
    return sorted_months_count


@login_required
def dashboard(request, device_type=None, selected_year=2023):
    # Get objects models for Device, Category, Brand, Entity
    devices_qs = Device.objects.all()
    categories_qs = Category.objects.all()
    brands_qs = Brand.objects.all()
    entities_qs = Entity.objects.all()

    print(selected_year)

    # Get devices by brand, entity and month
    devices_by_brand = get_devices_by_brand(brands_qs, devices_qs)
    devices_by_entities = get_devices_by_entities(entities_qs, devices_qs)
    months_count = count_devices_by_month(devices_qs, selected_year)
    devices_by_os = get_devices_by_os(devices_qs)

    # If device_type is specified, filter the devices by category and update
    # the devices values by brand, entity, and month
    if device_type:
        if device_type == 'All devices':
            new_devices_qs = devices_qs
        else:
            category = get_object_or_404(categories_qs, name=device_type)
            new_devices_qs = devices_qs.filter(product__category=category)

        devices_by_brand = get_devices_by_brand(brands_qs, new_devices_qs)
        devices_by_entities = get_devices_by_entities(entities_qs, new_devices_qs)
        devices_by_os = get_devices_by_os(new_devices_qs)

        if selected_year:
            months_count = count_devices_by_month(new_devices_qs, selected_year)

        # Prepare the data to be returned in the JsonResponse
        data = {
            'devices': [{'name': device.inventory.hostname} for device in new_devices_qs],
            'devices_by_brand': devices_by_brand,
            'devices_by_entities': devices_by_entities,
            'months_count': months_count,
            'devices_by_os': devices_by_os
        }
        return JsonResponse(data, safe=False)

    # If device_type is not specified, prepare the context to be passed to the template
    context = {
        'devices': devices_qs,
        'categories': categories_qs,
        'devices_by_brand': devices_by_brand,
        'devices_by_entities': devices_by_entities,
        'months_count': months_count,
        'devices_by_os': devices_by_os
    }

    # If request is an AJAX request, return a JsonResponse
    if request.is_ajax():
        return JsonResponse(context)

    # If request is not an AJAX request, render the template
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def show_device_table(request):
    devices = Device.objects.all()

    context = {
        'devices': devices,
    }

    return render(request, 'dashboard/show_device_table.html', context)


@login_required
def advanced_search(request):

    query = request.GET.get('search')
    form = SearchForm(request.GET)

    search_filter = None
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']

    brand_filter = request.GET.get('brand_filter')
    type_filter = request.GET.get('type_filter')
    user_link_filter = request.GET.get('radio_device_user')

    categories_qs = Category.objects.all()
    brand_qs = Brand.objects.all()

    if form.is_valid():
        result_process = None

        if query == '**':
            result_process = Device.objects.all()
        else:
            if search_filter == 'entity':
                result_process = Device.objects.filter(immo__location__site__name__icontains=query).order_by('added_date')
            elif search_filter == 'device':
                result_process = Device.objects.filter(
                    Q(immo__inventory_number__icontains=query) |
                    Q(inventory__hostname__icontains=query) |
                    Q(inventory__serial__icontains=query)
                ).order_by('added_date')
            elif search_filter == 'user':
                result_process = Device.objects.filter(
                    Q(device_user__last_name__icontains=query) |
                    Q(device_user__first_name__icontains=query) |
                    Q(device_user__uid__icontains=query)
                ).order_by('added_date')

        if user_link_filter == 'Without':
            result_process = result_process.filter(device_user__isnull=True)
        elif user_link_filter == 'With':
            result_process = result_process.filter(device_user__isnull=False)

        if not brand_filter == 'All':
            result_process = result_process.filter(product__brand__name__icontains=brand_filter)

        if not type_filter == 'All':
            result_process = result_process.filter(product__category__name__icontains=type_filter)

        context = {
            'form': form,
            'result_process': list(result_process),
            'categories': categories_qs,
            'brands': brand_qs,
        }

        print(context)
        return render(request, 'dashboard/advanced_search.html', context)

    context = {
        'form': form,
        'categories': categories_qs,
        'brands': brand_qs,
    }
    print('Form is not valid')
    return render(request, 'dashboard/advanced_search.html', context)
