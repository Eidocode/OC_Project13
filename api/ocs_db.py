from databases.database_manager import DatabaseManager

from tools import const, func_db


class OcsDbHandler:
    def __init__(self):
        self.devices = self.convert_to_array(self._get_raw_data_from_db())

    def _get_raw_data_from_db(self):
        ocs_db_manager = DatabaseManager(const.OCS_DB_NAME)
        this_query = """
            SELECT 
                db_inventory.hostname, db_inventory.serial, db_inventory.ram, 
                db_inventory.addr_mac, db_inventory.storage, db_product.name, 
                db_brand.name, db_category.name, db_cpu.name, db_cpu.frequency, 
                db_cpu.nb_cores, db_cpu_brand.name
            FROM
                db_inventory
            INNER JOIN db_product ON
                db_product.id = db_inventory.id_db_product
            INNER JOIN db_brand ON
                db_brand.id = db_product.id_db_brand
            INNER JOIN db_category ON
                db_category.id = db_product.id_db_category
            INNER JOIN db_cpu ON
                db_cpu.id = db_inventory.id_db_cpu
            INNER JOIN db_cpu_brand ON
                db_cpu_brand.id = db_cpu.id_db_cpu_brand"""
        return ocs_db_manager.get_query(this_query)

    def convert_to_array(self, raw_data):
        return [{
            'hostname': item[0],
            'serial': item[1],
            'ram': item[2],
            'addr_mac': item[3],
            'storage': item[4],
            'product': item[5],
            'brand': item[6],
            'catg': item[7],
            'cpu': item[8],
            'freq': item[9],
            'cores': item[10],
            'cpu_brand': item[11]
        } for item in raw_data]
