import requests

from django.core.management.base import BaseCommand

from random import randrange

from product.models import CpuBrand, Brand


class Command(BaseCommand):
    """
    """

    help = 'Adds new entries in oc_inventory database'
    pass
