import random
import sys

from api.immo_db import ImmoDbHandler
from api.inventory_db import InventoryDbHandler


class ControllerImmo:
    def __init__(self):
        self.immos_db_handler = ImmoDbHandler()
        self.inv_db_handler = InventoryDbHandler()

    def is_data_exist_in_table(self, table_name, p_key, data):
        """Checks that the specified data is already present in the database."""
        inv_table = self.inv_db_handler.get_data_from_table(table_name, p_key)
        return any(data == item['field'] for item in inv_table)

    def _set_enum_to_db_and_get_id(self):
        pass
