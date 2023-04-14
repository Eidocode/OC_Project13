"""
Script file used to populate the main database with data from the OCS and Immo
databases.
"""

from django.core.management.base import BaseCommand

from controllers.controller import Controller


class Command(BaseCommand):
    """
    Used to add a new parameter fill_db_from_ocs to manage.py
    """

    help = 'Specified the number of new entries to be created.(Default: 2)'

    def __init__(self):
        super().__init__()
        self.controller = Controller()

    def add_arguments(self, parser):
        """
        Adds int argument for command line
        """
        parser.add_argument(
            'nb_devices',
            type=int,
            nargs='?',
            default=2,
            help='Indicates the number of devices/immos to be created',
        )

    def handle(self, *args, **options):
        """
        Contains the method called when executed the command line (XXXX) with
        the specified int argument
        """
        nb_device = options['nb_devices']
        self.stdout.write(f"Processing for {nb_device} devices/immos...")
        self.controller.set_items_to_inventory_db(nb_device)
