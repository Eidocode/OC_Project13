from database.database_manager import DatabaseManager

from tools import const, func_db


class OcsDbHandler:
    def __init__(self):
        self.devices = func_db.convert_to_array(self._get_raw_data_from_db())

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
