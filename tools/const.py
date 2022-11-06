"""
File used to store the project constants
"""

import os


SRV_IP = os.environ.get('PSQL_SRV')
USER_ID = os.environ.get('DB_USER')
USER_PWD = os.environ.get('DB_PWD')
MAIN_DB_NAME = "inventory_test"
OCS_DB_NAME = "ocs_db"
IMMO_DB_NAME = "immo_db"
PSQL_PORT = '5432'
