"""
    Script file used to fill the main databases with data from the OCS external
    databases.
"""

from random import randrange

from django.core.management.base import BaseCommand

import requests

from product.models import Brand


class Command(BaseCommand):
    """
        Class used to add a new parameter fill_db_from_ocs to manage.py
    """

    help = 'Adds new entries in oc_inventory databases'

    def add_arguments(self, parser):
        """Adds int argument for command line"""

        parser.add_argument(
            'nb_devices',
            type=int,
            nargs='?',
            default=2,
            help='Indicates the number of categories to be created',
        )

    def handle(self, *args, **options):
        """Contains the method called when executed the command line
        (XXXX) with the specified int argument"""

        nb_dv = options['nb_devices']
        self.stdout.write(f"Processing for {nb_dv} devices...")
        # Launch class to execute

    