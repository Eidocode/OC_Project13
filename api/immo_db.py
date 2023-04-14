"""
Immo database handler
"""

from databases.database_manager import DatabaseManager
from tools import const


class ImmoDbHandler:
    """
    Interacts with the immo database and returns a list of containing the
    information for each item in the database.
    """
    def __init__(self):
        self.immos = self.convert_to_array(self._get_raw_data_from_db)

    @staticmethod
    def _get_raw_data_from_db():
        """
        Gets and returns a list of raw data from the source database.
        """
        immo_db_manager = DatabaseManager(const.IMMO_DB_NAME)
        this_query = """
            SELECT
                db_immo.bc_number, db_immo.inventory_number, db_immo.serial,
                db_user.first_name, db_user.last_name, db_user.uid,
                db_location.name, db_location.loc_number, db_entity.name,
                db_user.email, db_status.name, db_assignment.name
            FROM
                db_immo
            INNER JOIN db_user ON
                db_user.id = db_immo.id_db_user
            INNER JOIN db_location ON
                db_location.id = db_immo.id_db_location
            INNER JOIN db_entity ON
                db_entity.id = db_location.id_db_entity
            INNER JOIN db_status ON
                db_status.id = db_user.id_db_status
            INNER JOIN db_assignment ON
                db_assignment.id = db_user.id_db_assignment
            """
        return immo_db_manager.get_query(this_query)

    @staticmethod
    def convert_to_array(raw_data):
        """
        Converts the raw data from the source database into a list of
        dictionaries

        :param raw_data: The raw data from the source database
        :return: List of dictionaries containing the information for each item
        """
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
            'email': item[9],
            'status': item[10],
            'assignment': item[11],
        } for item in raw_data]
