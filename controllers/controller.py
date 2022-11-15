from controllers.controller_immo import ControllerImmo
from controllers.controller_ocs import ControllerOcs
from api.ocs_db import OcsDbHandler
from api.immo_db import ImmoDbHandler
from api.inventory_db import InventoryDbHandler

import tools.func_db


class Controller:
    def __init__(self):
        self.controller_immo = ControllerImmo()
        self.controller_ocs = ControllerOcs()
        self.ocs_db_handler = OcsDbHandler()
        self.immo_db_handler = ImmoDbHandler()
        self.inv_db_handler = InventoryDbHandler()

    def set_device_to_inventory_db(self, nb_devices):
        """Set all data to inventory db"""
        all_devices = self.ocs_db_handler.devices
        all_immos = self.immo_db_handler.immos

        devices_to_process = tools.func_db.get_x_line_from_data_lst(
            nb_devices, all_devices)

        for count, device in enumerate(devices_to_process, start=1):
            print(f"****** {count} ******")
            for immo in all_immos:
                if device['serial'] == immo['serial']:
                    device_user_id_val = self.controller_immo.set_device_user_to_db_and_get_id(immo)
                    immo_id_val = self.controller_immo.set_immo_to_db_and_get_id(immo)
                    inventory_id_val = self.controller_ocs.set_inventory_to_db_and_get_id(device)
                    product_id_val = self.controller_ocs.set_product_to_db_and_get_id(device)

                    self.inv_db_handler.set_data_to_device_table(
                        device_user_id_val, immo_id_val, inventory_id_val, product_id_val)


        # TODO Checks auto_now in models for added_date

        # if isinstance(data_to_set, dict):
        #     old_dict = data_to_set
        #     data_to_set = [old_dict]

        # device_user_id_val = self.controller_immo.set_device_user_to_db_and_get_id(data_to_set)
        # immo_id_val = self.controller_immo.set_immo_to_db_and_get_id(data_to_set)
        # inventory_id_val = self.controller_ocs.set_inventory_to_db_and_get_id(data_to_set)
        # product_id_val = self.controller_ocs.set_product_to_db_and_get_id(data_to_set)
        #
        # self.inv_db_handler.set_data_to_device_table(
        #     device_user_id_val, immo_id_val, inventory_id_val, product_id_val)
