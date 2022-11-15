from api.inventory_db import InventoryDbHandler

class ControllerImmo:
    def __init__(self):
        self.inv_db_handler = InventoryDbHandler()

    def is_data_exist_in_table(self, table_name, p_key, data):
        """Checks that the specified data is already present in the databases"""
        inv_table = self.inv_db_handler.get_data_from_table(table_name, p_key)
        return any(data == item['field'] for item in inv_table)

    def set_entity_to_db_and_get_id(self, data_to_check):
        """Retyrns entity id"""
        if self.is_data_exist_in_table(
                'product_entity', 'name', data_to_check['entity']):
            print('Item in product_entity already exists, getting id...')
            return self.inv_db_handler.get_id_field_from_table(
                'product_entity', 'name', data_to_check['entity']
            )
        print('Item in product_entity not exists, set data and get new id...')
        return self.inv_db_handler.set_data_to_entity_table_and_return_id(
            data_to_check['entity']
        )

    def set_location_to_db_and_get_id(self, data_to_check):
        """Returns location id"""
        entity_id_val = self.set_entity_to_db_and_get_id(data_to_check)
        if self.is_data_exist_in_table(
                'product_location', 'loc_number', data_to_check['loc_number']):
            print('Item in product_location already exists, getting id...')
            return self.inv_db_handler.get_id_field_from_table(
                'product_location', 'loc_number', data_to_check['loc_number']
            )
        print('Item in product_entity not exists, set data and get new id...')
        return self.inv_db_handler.set_data_to_location_table_and_return_id(
            data_to_check['location'], data_to_check['loc_number'],
            entity_id_val)

    def set_immo_to_db_and_get_id(self, data_to_check):
        """Returns immo id"""
        loc_id_val = self.set_location_to_db_and_get_id(data_to_check)
        if self.is_data_exist_in_table(
                'product_immo', 'inventory_number',
                data_to_check['inventory_number']):
            print('Item in product_immo already exists, getting id...')
            return self.inv_db_handler.get_id_field_from_table(
                'product_immo', 'inventory_number',
                data_to_check['inventory_number']
            )
        print('Item in product_immo not exists, set data and get new id...')
        return self.inv_db_handler.set_data_to_immo_table_and_return_id(
            data_to_check['bc_number'], data_to_check['inventory_number'],
            loc_id_val)

    def set_device_user_to_db_and_get_id(self, data_to_check):
        """Returns user id"""
        if self.is_data_exist_in_table(
                'product_deviceuser', 'uid', data_to_check['uid']):
            print('Item in product_deviceuser already exists, getting id...')
            return self.inv_db_handler.get_id_field_from_table(
                'product_deviceuser', 'uid', data_to_check['uid']
            )
        print('Item in product_deviceuser not exists, set data and get new id...')
        return self.inv_db_handler.set_data_to_deviceuser_table_and_return_id(
            data_to_check['first_name'], data_to_check['last_name'],
                data_to_check['uid'])
