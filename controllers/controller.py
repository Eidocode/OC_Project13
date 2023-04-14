"""
Gets the data returned by the Immo and Ocs controllers in order to insert them
into the main database.
"""

from controllers.controller_immo import ControllerImmo
from controllers.controller_ocs import ControllerDevice
from api.ocs_db import OcsDbHandler
from api.immo_db import ImmoDbHandler
from product.models import Device

import tools.func_db


class Controller:
    """
    Gets data from the other controllers and inserts them into the main
    database.
    """
    def __init__(self):
        self.immo_ctrl = ControllerImmo()
        self.device_ctrl = ControllerDevice()
        self.ocs_db_hdlr = OcsDbHandler()
        self.immo_db_hdlr = ImmoDbHandler()

    def set_items_to_inventory_db(self, nb_devices):
        """
        Set items to inventory db

        :param nb_devices: Number of devices to insert
        """
        all_devices = self.ocs_db_hdlr.devices  # Get all devices
        all_immos = self.immo_db_hdlr.immos  # Get all immos

        # Uses an external function to get x devices specified by nb_devices
        devices_to_process = tools.func_db.get_x_line_from_data_lst(
            nb_devices, all_devices)

        # Loops through devices_to_process and inserts the data into the db
        for count, device in enumerate(devices_to_process, start=1):
            print(f"****** {count}. {device['serial']} ******")
            for immo in all_immos:
                if device['serial'] == immo['serial']:
                    device_user = self.immo_ctrl.\
                        get_or_set_in_device_user_table(immo)
                    immo = self.immo_ctrl.get_or_set_in_immo_table(immo)
                    inventory = self.device_ctrl.get_or_set_in_inventory_table(
                        device)
                    product = self.device_ctrl.get_or_set_in_product_table(
                        device)

                    # Creates a new device if it doesn't exist in the db
                    Device.objects.get_or_create(
                        product=product, inventory=inventory,
                        device_user=device_user, immo=immo)
            print("")
