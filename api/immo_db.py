from databases.database_manager import DatabaseManager

from tools import const


class ImmoDbHandler:
    def __init__(self):
        self.immos = self.convert_to_array(self._get_raw_data_from_db())

    def _get_raw_data_from_db(self):
        immo_db_manager = DatabaseManager(const.IMMO_DB_NAME)
        this_query = """
            SELECT
                db_immo.bc_number, db_immo.inventory_number, db_immo.serial,
                db_user.first_name, db_user.last_name, db_user.uid,
                db_location.name, db_location.loc_number, db_entity.name
            FROM
                db_immo
            INNER JOIN db_user ON
                db_user.id = db_immo.id_db_user
            INNER JOIN db_location ON
                db_location.id = db_immo.id_db_location
            INNER JOIN db_entity ON
                db_entity.id = db_location.id_db_entity"""
        return immo_db_manager.get_query(this_query)

    def convert_to_array(self, raw_data):
        return [{
            'bc_number': item[0],
            'inventory_number': item[1],
            'serial': item[2],
            'first_name': item[3],
            'last_name': item[4],
            'uid': item[5],
            'location': item[6],
            'loc_number': item[7],
            'entity': item[8],
        } for item in raw_data]
