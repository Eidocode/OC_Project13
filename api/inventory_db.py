from database.database_manager import DatabaseManager

from tools import const


class InventoryDbHandler:
    def __init__(self):
        pass

    def get_data_from_table(self, table_name: str, field_to_check):
        db_manager = DatabaseManager(const.MAIN_DB_NAME)
        this_query = f"""SELECT id, {field_to_check} FROM {table_name}"""
        return [{
            'id': item[0],
            'field': item[1]
        } for item in list(db_manager.get_query(this_query))]

    def get_id_field_from_table(self, table_name, field_name, field_value):
        db_manager = DatabaseManager(const.MAIN_DB_NAME)
        this_query = f"""
            SELECT id 
            FROM {table_name} 
            WHERE {field_name} = '{field_value}'"""
        return db_manager.get_query(this_query)[0][0]

    def set_data_to_enum_table_and_return_id(self, table_name, field, value):
        db_manager = DatabaseManager(const.MAIN_DB_NAME)
        new_request = f"""INSERT INTO {table_name} ({field})
            VALUES ('{value}')"""
        db_manager.set_query(new_request)
        return self.get_id_field_from_table(table_name, field, value)

    def set_data_to_product_table_and_return_id(
            self, name_val, brand_id_val, category_id_val):
        db_manager = DatabaseManager(const.MAIN_DB_NAME)
        new_request = f"""
            INSERT INTO product_product (name, brand_id, category_id) 
            VALUES ('{name_val}', {brand_id_val}, {category_id_val})"""
        db_manager.set_query(new_request)
        return self.get_id_field_from_table('product_product', 'name', name_val)

    def set_data_to_cpu_table_and_return_id(
            self, cpu_brand_id_val, name_val, freq_val,  core_val):
        db_manager = DatabaseManager(const.MAIN_DB_NAME)
        freq_val = round(float(freq_val), 2)
        new_request = f"""
            INSERT INTO product_cpu (cpu_brand_id, name, frequency, nb_cores) 
            VALUES ({cpu_brand_id_val}, '{name_val}', {freq_val}, {core_val})"""
        db_manager.set_query(new_request)
        return self.get_id_field_from_table('product_cpu', 'name', name_val)

    def set_data_to_inventory_table_and_return_id(
            self, hostname_val, serial_val, cpu_id_val, ram_val, addr_mac_val,
                strorage_val):
        db_manager = DatabaseManager(const.MAIN_DB_NAME)
        new_request = f"""
            INSERT INTO product_inventory (hostname, serial, cpu_id, ram, 
                addr_mac, storage) 
            VALUES ('{hostname_val}', '{serial_val}', {cpu_id_val}, {ram_val}, 
                '{addr_mac_val}', {strorage_val})
        """
        db_manager.set_query(new_request)
        return self.get_id_field_from_table(
            'product_inventory', 'serial', serial_val)



