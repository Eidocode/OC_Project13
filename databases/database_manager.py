"""
File used to manage external databases
"""

import psycopg2

from tools import const


class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.psql_connex = psycopg2.connect(
            host=const.SRV_IP,
            database=self.db_name,
            user=const.USER_ID,
            password=const.USER_PWD,
            port=const.PSQL_PORT,
        )

    def get_query(self, query):
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
