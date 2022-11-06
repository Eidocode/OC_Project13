from database.database_manager import DatabaseManager

from tools import const


class OcsDbHandler:
    def __init__(self):
        self.ocs_db_manager = DatabaseManager(const.OCS_DB_NAME)

    @property
    def _get_all_devices(self):
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

        return self.ocs_db_manager.get_query(this_query)

    def convert_data_to_array(self):
        lst_devices = self._get_all_devices
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
        } for item in lst_devices]


ocs_handler = OcsDbHandler()
print(ocs_handler.convert_data_to_array())
