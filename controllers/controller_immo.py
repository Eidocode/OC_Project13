from product.models import Entity, Location, Immo, DeviceUser

class ControllerImmo:

    def get_or_set_in_device_user_table(self, data_to_check):
        """Returns data_to_check id in Immo model"""
        fname = data_to_check['first_name']
        lname = data_to_check['last_name']
        uid = data_to_check['uid']
        this_data = DeviceUser.objects.get_or_create(
            first_name=fname,
            last_name=lname, uid=uid)
        print(f"Added user {fname} {lname} with uid {uid}")
        return this_data[0]

    def _get_or_set_in_entity_table(self, data_to_check):
        """Returns data_to_check id in Entity model"""
        this_data = Entity.objects.get_or_create(name=data_to_check['entity'])
        return this_data[0]

    def _get_or_set_in_location_table(self, data_to_check):
        """Returns data_to_check id in Location model"""
        entity_instance = self._get_or_set_in_entity_table(data_to_check)
        this_data = Location.objects.get_or_create(
            name=data_to_check['location'],
            loc_number=data_to_check['loc_number'], site=entity_instance)
        return this_data[0]

    def get_or_set_in_immo_table(self, data_to_check):
        """Returns data_to_check id in Immo model"""
        location_instance = self._get_or_set_in_location_table(data_to_check)
        this_data = Immo.objects.get_or_create(
            bc_number=data_to_check['bc_number'],
            inventory_number=data_to_check['inventory_number'],
            location=location_instance)
        return this_data[0]
