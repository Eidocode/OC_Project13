from django.shortcuts import render

from product.models import DeviceUser


def show_product_user(request):
    """
    Used for product_user page
    """
    users = DeviceUser.objects.filter().order_by('-id')[:10]

    context = {
        'device_users': users
    }
    return render(request, 'product_user.html', context)

def show_user_info(request):
    return render(request, 'user_info.html')