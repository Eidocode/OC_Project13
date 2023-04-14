"""
Function used to return x lines from a data list
"""
import random
import sys


def get_x_line_from_data_lst(nb_item: int, db_handler_data):
    """
    Gets x lines from a data list and return it

    :param nb_item: number of items to return
    :param db_handler_data: list of data from database
    :return: Returns a list with x lines from the data list
    """
    lst_index = []  # List of indexes
    # Check if nb_item is greater than 0
    if nb_item <= 0:
        sys.exit("nb_item must be greater than 0...")

    # Gets random indexes from the data list
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
