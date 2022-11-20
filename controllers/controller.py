from controllers.controller_immo import ControllerImmo
from controllers.controller_ocs import ControllerDevice
from api.ocs_db import OcsDbHandler
from api.immo_db import ImmoDbHandler
from product.models import Device

import tools.func_db


class Controller:
    def __init__(self):
        self.controller_immo = ControllerImmo()
        self.controller_device = ControllerDevice()
        self.ocs_db_handler = OcsDbHandler()
        self.immo_db_handler = ImmoDbHandler()

    def set_items_to_inventory_db(self, nb_devices):
        """Set all data to inventory db"""
        all_devices = self.ocs_db_handler.devices
        all_immos = self.immo_db_handler.immos

        devices_to_process = tools.func_db.get_x_line_from_data_lst(
            nb_devices, all_devices)

        for count, device in enumerate(devices_to_process, start=1):
            print(f"****** {count} ******")
            for immo in all_immos:
                if device['serial'] == immo['serial']:
                    device_user_instance = self.controller_immo.get_or_set_in_device_user_table(immo)
                    immo_instance = self.controller_immo.get_or_set_in_immo_table(immo)
                    inventory_instance = self.controller_device.get_or_set_in_inventory_table(device)
                    product_instance = self.controller_device.get_or_set_in_product_table(device)
                    Device.objects.get_or_create(
                        product= product_instance, inventory=inventory_instance,
                        device_user=device_user_instance, immo= immo_instance)
            print("")

        # TODO :
        #   - Checks auto_now in models for added_date
        #   - Adds only new devices :
        #       - device['product']
        #       - device['inventory']
        #       - immo['immo']
        #   - Adds only new users :
        #       - immo['device_user']
