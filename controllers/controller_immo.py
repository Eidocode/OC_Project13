"""
Gets data from the main database and checks if the new data already exists, if
not, adds it to the database. (Immo)
"""

from product.models import Entity, Location, Immo, DeviceUser, Status,\
    Assignment


class ControllerImmo:
    """
    Gets data from the IMMO database and sets it in the main database if it
    does not already exist.
    """

    def get_or_set_in_device_user_table(self, data_to_check):
        """
        Returns data_to_check id in DeviceUser model and creates it if not
        exist.
        """
        fname = data_to_check['first_name']
        lname = data_to_check['last_name']
        uid = data_to_check['uid']
        email = data_to_check['email']
        status = self._get_or_set_in_status_table(data_to_check)
        assignment = self._get_or_set_in_assignment_table(data_to_check)
        this_data = DeviceUser.objects.get_or_create(
            first_name=fname, last_name=lname, email=email,
            uid=uid, status=status, assignment=assignment
        )
        print(f"Added user {fname} {lname} with uid {uid} ({email})")
        return this_data[0]

    @staticmethod
    def _get_or_set_in_status_table(data_to_check):
        """
        Returns data_to_check id in Status model and creates it if not exist.
        """
        this_data = Status.objects.get_or_create(name=data_to_check['status'])
        return this_data[0]

    @staticmethod
    def _get_or_set_in_assignment_table(data_to_check):
        """
        Returns data_to_check id in Assignment model and creates it if not
        exist.
        """
        this_data = Assignment.objects.get_or_create(
            name=data_to_check['assignment']
        )
        return this_data[0]

    @staticmethod
    def _get_or_set_in_entity_table(data_to_check):
        """
        Returns data_to_check id in Entity model and creates it if not exist.
        """
        this_data = Entity.objects.get_or_create(name=data_to_check['entity'])
        return this_data[0]

    def _get_or_set_in_location_table(self, data_to_check):
        """
        Returns data_to_check id in Location model and creates it if not exist.
        """
        entity_instance = self._get_or_set_in_entity_table(data_to_check)
        this_data = Location.objects.get_or_create(
            name=data_to_check['location'],
            loc_number=data_to_check['loc_number'], site=entity_instance)
        return this_data[0]

    def get_or_set_in_immo_table(self, data_to_check):
        """
        Returns data_to_check id in Immo model and creates it if not exist.
        """
        loc_instance = self._get_or_set_in_location_table(data_to_check)
        bc_num = data_to_check['bc_number']
        inv_num = data_to_check['inventory_number']
        this_data = Immo.objects.get_or_create(
            bc_number=bc_num,
            inventory_number=inv_num,
            location=loc_instance)
        print(f"Added BC N°{bc_num} with immo {inv_num}")
        return this_data[0]
