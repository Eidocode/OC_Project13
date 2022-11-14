import random
import sys

from api.ocs_db import OcsDbHandler
from api.inventory_db import InventoryDbHandler


class ControllerOcs:
    def __init__(self):
        self.ocs_db_handler = OcsDbHandler()
        self.inv_db_handler = InventoryDbHandler()

    def is_data_exist_in_table(self, table_name, p_key, data):
        """Checks that the specified data is already present in the database."""
        inv_table = self.inv_db_handler.get_data_from_table(table_name, p_key)
        return any(data == item['field'] for item in inv_table)

    def _set_enum_to_db_and_get_id(self, table_name, field_name, data_to_check):
        """Return id for enum tables (brand, category, cpu_brand)"""
        if self.is_data_exist_in_table(table_name, field_name, data_to_check):
            print(f'Item in {table_name} already exists, getting id...')
            return self.inv_db_handler.get_id_field_from_table(
                table_name, field_name, data_to_check
            )
        print(f'Item in {table_name} not exists, set data and get new id...')
        return self.inv_db_handler.set_data_to_enum_table_and_return_id(
            table_name, field_name, data_to_check
        )

    def set_brand_to_db_and_get_id(self, data_to_check):
        """Returns brand id"""
        return self._set_enum_to_db_and_get_id(
            'product_brand', 'name', data_to_check['brand']
        )

    def set_category_to_db_and_get_id(self, data_to_check):
        """Returns Category id"""
        return self._set_enum_to_db_and_get_id(
            'product_category', 'name', data_to_check['catg']
        )

    def set_cpu_brand_to_db_and_get_id(self, data_to_check):
        """Returns CPU Brand id"""
        return self._set_enum_to_db_and_get_id(
            'product_cpubrand', 'name', data_to_check['cpu_brand']
        )

    def set_product_to_db_and_get_id(self, data_to_check):
        """Returns Product id"""
        brand_id_val = self.set_brand_to_db_and_get_id(data_to_check)
        catg_id_val = self.set_category_to_db_and_get_id(data_to_check)
        print(f"Brand_id : {brand_id_val}, catg_id : {catg_id_val}")
        if self.is_data_exist_in_table(
                'product_product', 'name', data_to_check['product']):
            print('Item in product_product already exists, getting id...')
            return self.inv_db_handler.get_id_field_from_table(
                'product_product', 'name', data_to_check['product']
            )
        print('Item in product_product not exists, set data and get new id...')
        return self.inv_db_handler.set_data_to_product_table_and_return_id(
            data_to_check['product'], brand_id_val, catg_id_val
        )

    def set_cpu_to_db_and_get_id(self, data_to_check):
        """Returns Product id"""
        cpu_brand_id_val = self.set_cpu_brand_to_db_and_get_id(data_to_check)
        print(f"Cpu_brand_id : {cpu_brand_id_val}")
        if self.is_data_exist_in_table(
                'product_cpu', 'name', data_to_check['cpu']):
            print('Item in product_cpu already exists, getting id...')
            return self.inv_db_handler.get_id_field_from_table(
                'product_cpu', 'name', data_to_check['cpu']
            )
        print('Item in product_cpu not exists, set data and get new id...')
        return self.inv_db_handler.set_data_to_cpu_table_and_return_id(
            cpu_brand_id_val,
            data_to_check['cpu'],
            data_to_check['freq'],
            data_to_check['cores']
        )

    def set_inventory_to_db_and_get_id(self, data_to_check):
        """Returns Inventory id"""
        cpu_id_val = self.set_cpu_to_db_and_get_id(data_to_check)
        print(f'Cpu_id : {cpu_id_val}')
        if self.is_data_exist_in_table(
                'product_inventory', 'serial', data_to_check['serial']):
            print('Item in product_inventory already exists, getting id...')
            return self.inv_db_handler.get_id_field_from_table(
                'product_inventory', 'serial', data_to_check['serial']
            )
        print('Item in product_inventory not exists, set data and get new id...')
        return self.inv_db_handler.set_data_to_inventory_table_and_return_id(
            data_to_check['hostname'],
            data_to_check['serial'],
            cpu_id_val,
            data_to_check['ram'],
            data_to_check['addr_mac'],
            data_to_check['storage'],
        )
