"""
Used to manage the connection of external databases
"""

import psycopg2

from tools import const


class DatabaseManager:
    """
    External database connection manager
    """
    def __init__(self, db_name):
        self.db_name = db_name  # Database name specified by db_name
        # Database connection
        self.psql_connex = psycopg2.connect(
            host=const.SRV_IP,  # Database server IP
            database=self.db_name,  # Database name
            user=const.USER_ID,  # Database user
            password=const.USER_PWD,  # Database user password
            port=const.PSQL_PORT,  # Database port
        )

    def get_query(self, query):
        """
        SQL query to get data from a database

        :param query: query to be sent
        :return: List of raw data
        """
        result = None
        try:
            cursor = self.psql_connex.cursor()
            print(f'Connection established with {self.db_name}...')
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
        except psycopg2.InterfaceError as error:
            print(f'Error on {self.db_name}...')
            print(error)
        finally:
            self.psql_connex.close()
            print(f'Connection closed with {self.db_name}...')

        return result

    def set_query(self, query):
        """
        SQL query to set data to a database

        :param query: query to be sent
        """
        try:
            cursor = self.psql_connex.cursor()
            print("Connection Established...")
            cursor.execute(query)
            print(f'{str(cursor.rowcount)} QUERY SUCCESS...')
            self.psql_connex.commit()
            cursor.close()
        except psycopg2.InterfaceError as error:
            print(f'Error on {self.db_name}...')
            print(error)
        finally:
            self.psql_connex.close()
            print(f'Connection closed with {self.db_name}...')

    def _reset(self):
        self.__init__(self.db_name)

    def _destroy(self):
        del self
