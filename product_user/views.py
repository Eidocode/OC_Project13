from django.shortcuts import render, get_object_or_404

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


def show_user_info(request, user_id):
    """
    Used for user_info page
    """

    # Gets a user designated by product_id or returns 404
    user = get_object_or_404(DeviceUser, pk=user_id)

    context = {
        'user': user
    }

    return render(request, 'user_info.html', context)
