import random
import sys


def get_x_line_from_data_lst(nb_item: int, db_handler_data):
    """Returns x lines of data specified in the parameters"""
    lst_index = []
    if nb_item <= 0:
        sys.exit("nb_item must be greater than 0...")
    for _ in range(nb_item):
        new_index = random.randrange(0, len(db_handler_data))
        while new_index in lst_index:
            new_index = random.randrange(
                0, len(db_handler_data)
            )
        lst_index.append(new_index)
    if nb_item == 1:
        return db_handler_data[lst_index[0]]
    return [db_handler_data[_] for _ in lst_index]


# def get_data_from_table(db_manager, table_name):
#     this_db_manager = DatabaseManager(db_manager)
#     this_query = f"""SELECT * FROM {table_name}"""
#     return [item[0] for item in this_db_manager.get_query(this_query)]
