from product.models import Brand, Category, CpuBrand, Product, Cpu, Inventory



class ControllerDevice:

    def _get_or_set_in_brand_table(self, data_to_check):
        """Returns data_to_check id in Brand model"""
        this_data = Brand.objects.get_or_create(name=data_to_check['brand'])
        return this_data[0]

    def _get_or_set_in_category_table(self, data_to_check):
        """Returns data_to_check id in Category model"""
        this_data = Category.objects.get_or_create(name=data_to_check['catg'])
        return this_data[0]

    def _get_or_set_in_cpu_brand_table(self, data_to_check):
        """Returns data_to_check id in Cpubrand model"""
        this_data = CpuBrand.objects.get_or_create(name=data_to_check['cpu_brand'])
        return this_data[0]

    def get_or_set_in_product_table(self, data_to_check):
        """Returns data_to_check id in Product model"""
        brand_instance = self._get_or_set_in_brand_table(data_to_check)
        catg_instance = self._get_or_set_in_category_table(data_to_check)
        product = data_to_check['product']
        this_data = Product.objects.get_or_create(
            name=product, brand=brand_instance,
            category=catg_instance)
        print(f"Added {product}")
        return this_data[0]

    def _get_or_set_in_cpu_table(self, data_to_check):
        """Returns data_to_check id in Cpu model"""
        cpu_brand_instance = self._get_or_set_in_cpu_brand_table(data_to_check)
        # freq = round(float(data_to_check['freq']), 2)
        this_data = Cpu.objects.get_or_create(cpu_brand=cpu_brand_instance,
                                              name=data_to_check['cpu'],
                                              frequency=data_to_check['freq'],
                                              nb_cores=data_to_check['cores'])
        return this_data[0]

    def get_or_set_in_inventory_table(self, data_to_check):
        """Returns data_to_check id in Inventory model"""
        cpu_instance = self._get_or_set_in_cpu_table(data_to_check)
        host = data_to_check['hostname']
        serial = data_to_check['serial']
        ram = data_to_check['ram']
        storage = data_to_check['storage']
        this_data = Inventory.objects.get_or_create(
            hostname=host, serial=serial,
            cpu=cpu_instance, ram=ram,
            addr_mac=data_to_check['addr_mac'], storage=data_to_check['storage']
        )
        print(f"Added device {host} with serial {serial}")
        return this_data[0]
