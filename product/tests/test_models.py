from django.test import TestCase

from product.models import Brand, Category, Product, CpuBrand, Cpu, Inventory, \
    Status, Assignment, DeviceUser, Entity, Location, Immo


class BrandModelTest(TestCase):
    """
    Test the Brand model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        Brand.objects.create(name="Brand1")

    def test_name_max_length(self):
        """
        Test the Brand name max_length.
        """
        brand = Brand.objects.get(id=1)
        max_length = brand._meta.get_field('name').max_length
        self.assertEqual(max_length, 15)

    def test_name_is_unique(self):
        """
        Test the Brand name is_unique.
        """
        brand = Brand.objects.get(id=1)
        is_unique = brand._meta.get_field('name').unique
        self.assertTrue(is_unique)

    def test_name_is_name(self):
        """
        Test the Brand name blank.
        """
        brand = Brand.objects.get(id=1)
        self.assertEqual(brand.name, 'Brand1')

    def test_name_is_not_name(self):
        """
        Test the Brand name blank.
        """
        brand = Brand.objects.get(id=1)
        self.assertNotEqual(brand.name, 'Brand2')


class CategoryModelTest(TestCase):
    """
    Test the Category model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        Category.objects.create(name="Category1")

    def test_name_max_length(self):
        """
        Test the Category name max_length.
        """
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 15)

    def test_name_is_unique(self):
        """
        Test the Category name is_unique.
        """
        category = Category.objects.get(id=1)
        is_unique = category._meta.get_field('name').unique
        self.assertTrue(is_unique)

    def test_name_is_name(self):
        """
        Test the Brand name blank.
        """
        category = Category.objects.get(id=1)
        self.assertEqual(category.name, 'Category1')

    def test_name_is_not_name(self):
        """
        Test the Brand name blank.
        """
        category = Category.objects.get(id=1)
        self.assertNotEqual(category.name, 'Category2')


class ProductModelTest(TestCase):
    """
    Test the Product model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        Product.objects.create(
            brand=Brand.objects.create(name='Brand1'),
            category=Category.objects.create(name='Category1'),
            name="Product1",
        )

    def test_name_max_length(self):
        """
        Test the Product name max_length.
        """
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 25)

    def test_name_is_unique(self):
        """
        Test the Product name is_unique.
        """
        product = Product.objects.get(id=1)
        is_unique = product._meta.get_field('name').unique
        self.assertTrue(is_unique)

    def test_name_is_name(self):
        """
        Test the Brand name blank.
        """
        product = Product.objects.get(id=1)
        self.assertEqual(product.name, 'Product1')

    def test_name_is_not_name(self):
        """
        Test the Brand name blank.
        """
        product = Product.objects.get(id=1)
        self.assertNotEqual(product.name, 'Product2')


class CpuBrandModelTest(TestCase):
    """
    Test the Brand model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        CpuBrand.objects.create(name="CpuBrand1")

    def test_name_max_length(self):
        """
        Test the Brand name max_length.
        """
        cpu_brand = CpuBrand.objects.get(id=1)
        max_length = cpu_brand._meta.get_field('name').max_length
        self.assertEqual(max_length, 20)

    def test_name_is_unique(self):
        """
        Test the Brand name is_unique.
        """
        cpu_brand = CpuBrand.objects.get(id=1)
        is_unique = cpu_brand._meta.get_field('name').unique
        self.assertTrue(is_unique)

    def test_name_is_name(self):
        """
        Test the Brand name blank.
        """
        cpu_brand = CpuBrand.objects.get(id=1)
        self.assertEqual(cpu_brand.name, 'CpuBrand1')

    def test_name_is_not_name(self):
        """
        Test the Brand name blank.
        """
        cpu_brand = CpuBrand.objects.get(id=1)
        self.assertNotEqual(cpu_brand.name, 'CpuBrand2')


class CpuModelTest(TestCase):
    """
    Test the Cpu model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        Cpu.objects.create(
            cpu_brand=CpuBrand.objects.create(name='Brand1'),
            name="Cpu1",
            frequency=3.21,
            nb_cores=8,
        )

    def test_name_max_length(self):
        """
        Test the Cpu name max_length.
        """
        cpu = Cpu.objects.get(id=1)
        max_length = cpu._meta.get_field('name').max_length
        self.assertEqual(max_length, 20)

    def test_name_is_unique(self):
        """
        Test the Cpu name is_unique.
        """
        cpu = Cpu.objects.get(id=1)
        is_unique = cpu._meta.get_field('name').unique
        self.assertTrue(is_unique)

    def test_name_is_name(self):
        """
        Test the Brand name blank.
        """
        cpu = Cpu.objects.get(id=1)
        self.assertEqual(cpu.name, 'Cpu1')

    def test_name_is_not_name(self):
        """
        Test the Brand name blank.
        """
        cpu = Cpu.objects.get(id=1)
        self.assertNotEqual(cpu.name, 'Cpu2')

    def test_frequency_is_frequency(self):
        """
        Test the Brand name blank.
        """
        cpu = Cpu.objects.get(id=1)
        self.assertEqual(float(cpu.frequency), 3.21)

    def test_frequency_is_not_frequency(self):
        """
        Test the Brand name blank.
        """
        cpu = Cpu.objects.get(id=1)
        self.assertNotEqual(float(cpu.frequency), 3.22)

    def test_nb_cores_is_nb_cores(self):
        """
        Test the Brand name blank.
        """
        cpu = Cpu.objects.get(id=1)
        self.assertEqual(cpu.nb_cores, 8)

    def test_nb_cores_is_not_nb_cores(self):
        """
        Test the Brand name blank.
        """
        cpu = Cpu.objects.get(id=1)
        self.assertNotEqual(cpu.nb_cores, 9)


class InventoryModelTest(TestCase):
    """
    Test the Inventory model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        Inventory.objects.create(
            cpu=Cpu.objects.create(
                cpu_brand=CpuBrand.objects.create(name='Brand1'),
                name="Cpu1",
                frequency=3.21,
                nb_cores=8,
            ),
            ram=16,
            storage=512,
            hostname="Hostname1",
            serial="Serial1",
            addr_mac="Mac1",
        )
        Inventory.objects.create(
            cpu=Cpu.objects.create(
                cpu_brand=CpuBrand.objects.create(name='Brand2'),
                name="Cpu2",
                frequency=2.31,
                nb_cores=12,
            ),
            ram=None,
            storage=None,
            hostname="Hostname2",
            serial="Serial2",
            addr_mac=None,
        )

    def test_hostname_max_length(self):
        """
        Test the Inventory hostname max_length.
        """
        inventory = Inventory.objects.get(id=1)
        max_length = inventory._meta.get_field('hostname').max_length
        self.assertEqual(max_length, 20)

    def test_hostname_is_hostname(self):
        """
        Test the Brand name blank.
        """
        inventory = Inventory.objects.get(id=1)
        self.assertEqual(inventory.hostname, 'Hostname1')

    def test_hostname_is_not_hostname(self):
        """
        Test the Brand name blank.
        """
        inventory = Inventory.objects.get(id=1)
        self.assertNotEqual(inventory.hostname, 'Hostname2')

    def test_serial_max_length(self):
        """
        Test the Inventory serial max_length.
        """
        inventory = Inventory.objects.get(id=1)
        max_length = inventory._meta.get_field('serial').max_length
        self.assertEqual(max_length, 20)

    def test_serial_is_unique(self):
        """
        Test the Inventory serial is_unique.
        """
        inventory = Inventory.objects.get(id=1)
        is_unique = inventory._meta.get_field('serial').unique
        self.assertTrue(is_unique)

    def test_serial_is_serial(self):
        """
        Test the Brand name blank.
        """
        inventory = Inventory.objects.get(id=1)
        self.assertEqual(inventory.serial, 'Serial1')

    def test_serial_is_not_serial(self):
        """
        Test the Brand name blank.
        """
        inventory = Inventory.objects.get(id=1)
        self.assertNotEqual(inventory.serial, 'Serial2')

    def test_ram_is_ram(self):
        """
        Test the Brand name blank.
        """
        inventory = Inventory.objects.get(id=1)
        self.assertEqual(inventory.ram, 16)

    def test_ram_is_not_ram(self):
        """
        Test the Brand name blank.
        """
        inventory = Inventory.objects.get(id=1)
        self.assertNotEqual(inventory.ram, 17)

    def test_ram_is_null(self):
        """
        Test the Brand name blank.
        """
        inventory = Inventory.objects.get(id=2)
        self.assertIsNone(inventory.ram)

    def test_addr_mac_is_addr_mac(self):
        """
        Test the Brand name blank.
        """
        inventory = Inventory.objects.get(id=1)
        self.assertEqual(inventory.addr_mac, 'Mac1')

    def test_addr_mac_is_not_addr_mac(self):
        """
        Test the Brand name blank.
        """
        inventory = Inventory.objects.get(id=1)
        self.assertNotEqual(inventory.addr_mac, 'Mac2')

    def test_addr_mac_is_unique(self):
        """
        Test the Brand name blank.
        """
        inventory = Inventory.objects.get(id=1)
        is_unique = inventory._meta.get_field('addr_mac').unique
        self.assertTrue(is_unique)

    def test_addr_mac_is_null(self):
        """
        Test the Brand name blank.
        """
        inventory = Inventory.objects.get(id=2)
        self.assertIsNone(inventory.addr_mac)

    def test_storage_is_storage(self):
        """
        Test the Brand name blank.
        """
        inventory = Inventory.objects.get(id=1)
        self.assertEqual(inventory.storage, 512)

    def test_storage_is_not_storage(self):
        """
        Test the Brand name blank.
        """
        inventory = Inventory.objects.get(id=1)
        self.assertNotEqual(inventory.storage, 256)

    def test_storage_is_null(self):
        """
        Test the Brand name blank.
        """
        inventory = Inventory.objects.get(id=2)
        self.assertIsNone(inventory.storage)


class StatusModelTest(TestCase):
    """
    Test the Status model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        Status.objects.create(
            name="Status1",
        )

    def test_name_max_length(self):
        """
        Test the Status name max_length.
        """
        status = Status.objects.get(id=1)
        max_length = status._meta.get_field('name').max_length
        self.assertEqual(max_length, 20)

    def test_name_is_unique(self):
        """
        Test the Status name is_unique.
        """
        status = Status.objects.get(id=1)
        is_unique = status._meta.get_field('name').unique
        self.assertTrue(is_unique)

    def test_name_is_name(self):
        """
        Test the Brand name blank.
        """
        status = Status.objects.get(id=1)
        self.assertEqual(status.name, 'Status1')

    def test_name_is_not_name(self):
        """
        Test the Brand name blank.
        """
        status = Status.objects.get(id=1)
        self.assertNotEqual(status.name, 'Status2')


class AssignmentModelTest(TestCase):
    """
    Test the Assignment model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        Assignment.objects.create(
            name="Assignment1",
        )

    def test_name_is_unique(self):
        """
        Test the Assignment name is_unique.
        """
        assignment = Assignment.objects.get(id=1)
        is_unique = assignment._meta.get_field('name').unique
        self.assertTrue(is_unique)

    def test_name_max_length(self):
        """
        Test the Assignment name max_length.
        """
        assignment = Assignment.objects.get(id=1)
        max_length = assignment._meta.get_field('name').max_length
        self.assertEqual(max_length, 15)

    def test_name_is_name(self):
        """
        Test the Brand name blank.
        """
        assignment = Assignment.objects.get(id=1)
        self.assertEqual(assignment.name, 'Assignment1')

    def test_name_is_not_name(self):
        """
        Test the Brand name blank.
        """
        assignment = Assignment.objects.get(id=1)
        self.assertNotEqual(assignment.name, 'Assignment2')


class DeviceUserModelTest(TestCase):
    """
    Test the DeviceUser model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        DeviceUser.objects.create(
            first_name="fname1",
            last_name="lname1",
            email="email1",
            uid="uid1",
        )
        DeviceUser.objects.create(
            first_name="fname2",
            last_name="lname2",
            email=None,
            uid="uid2",
        )

    def test_first_name_max_length(self):
        """
        Test the DeviceUser first_name max_length.
        """
        device_user = DeviceUser.objects.get(id=1)
        max_length = device_user._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 15)

    def test_first_name_is_first_name(self):
        """
        Test the Brand name blank.
        """
        device_user = DeviceUser.objects.get(id=1)
        self.assertEqual(device_user.first_name, 'fname1')

    def test_first_name_is_not_first_name(self):
        """
        Test the Brand name blank.
        """
        device_user = DeviceUser.objects.get(id=1)
        self.assertNotEqual(device_user.first_name, 'fname2')

    def test_last_name_max_length(self):
        """
        Test the DeviceUser last_name max_length.
        """
        device_user = DeviceUser.objects.get(id=1)
        max_length = device_user._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 15)

    def test_last_name_is_last_name(self):
        """
        Test the Brand name blank.
        """
        device_user = DeviceUser.objects.get(id=1)
        self.assertEqual(device_user.last_name, 'lname1')

    def test_last_name_is_not_last_name(self):
        """
        Test the Brand name blank.
        """
        device_user = DeviceUser.objects.get(id=1)
        self.assertNotEqual(device_user.last_name, 'lname2')

    def test_email_max_length(self):
        """
        Test the DeviceUser email max_length.
        """
        device_user = DeviceUser.objects.get(id=1)
        max_length = device_user._meta.get_field('email').max_length
        self.assertEqual(max_length, 70)

    def test_email_is_email(self):
        """
        Test the Brand name blank.
        """
        device_user = DeviceUser.objects.get(id=1)
        self.assertEqual(device_user.email, 'email1')

    def test_email_is_not_email(self):
        """
        Test the Brand name blank.
        """
        device_user = DeviceUser.objects.get(id=1)
        self.assertNotEqual(device_user.email, 'email2')

    def test_email_is_unique(self):
        """
        Test the DeviceUser email is_unique.
        """
        device_user = DeviceUser.objects.get(id=1)
        is_unique = device_user._meta.get_field('email').unique
        self.assertTrue(is_unique)

    def test_email_is_null(self):
        """
        Test the Brand name blank.
        """
        device_user = DeviceUser.objects.get(id=2)
        self.assertIsNone(device_user.email)

    def test_uid_max_length(self):
        """
        Test the DeviceUser uid max_length.
        """
        device_user = DeviceUser.objects.get(id=1)
        max_length = device_user._meta.get_field('uid').max_length
        self.assertEqual(max_length, 10)

    def test_uid_is_uid(self):
        """
        Test the Brand name blank.
        """
        device_user = DeviceUser.objects.get(id=1)
        self.assertEqual(device_user.uid, 'uid1')

    def test_uid_is_not_uid(self):
        """
        Test the Brand name blank.
        """
        device_user = DeviceUser.objects.get(id=1)
        self.assertNotEqual(device_user.uid, 'uid2')

    def test_uid_is_unique(self):
        """
        Test the DeviceUser uid is_unique.
        """
        device_user = DeviceUser.objects.get(id=1)
        is_unique = device_user._meta.get_field('uid').unique
        self.assertTrue(is_unique)

    def test_status_is_null(self):
        """
        Test the Brand name blank.
        """
        device_user = DeviceUser.objects.get(id=2)
        self.assertIsNone(device_user.status)

    def test_assignment_is_null(self):
        """
        Test the Brand name blank.
        """
        device_user = DeviceUser.objects.get(id=2)
        self.assertIsNone(device_user.assignment)


class EntityModelTest(TestCase):
    """
    Test the Entity model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        Entity.objects.create(
            name="Entity1",
        )

    def test_name_max_length(self):
        """
        Test the Entity name max_length.
        """
        entity = Entity.objects.get(id=1)
        max_length = entity._meta.get_field('name').max_length
        self.assertEqual(max_length, 15)

    def test_name_is_name(self):
        """
        Test the Brand name blank.
        """
        entity = Entity.objects.get(id=1)
        self.assertEqual(entity.name, 'Entity1')

    def test_name_is_not_name(self):
        """
        Test the Brand name blank.
        """
        entity = Entity.objects.get(id=1)
        self.assertNotEqual(entity.name, 'Entity2')

    def test_name_is_unique(self):
        """
        Test the Entity name is_unique.
        """
        entity = Entity.objects.get(id=1)
        is_unique = entity._meta.get_field('name').unique
        self.assertTrue(is_unique)


class LocationModelTest(TestCase):
    """
    Test the Location model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        Location.objects.create(
            name="Loc1",
            loc_number=1,
            site=Entity.objects.create(
                name="Entity1",
            )
        )

    def test_name_max_length(self):
        """
        Test the Location name max_length.
        """
        location = Location.objects.get(id=1)
        max_length = location._meta.get_field('name').max_length
        self.assertEqual(max_length, 6)

    def test_name_is_name(self):
        """
        Test the Brand name blank.
        """
        location = Location.objects.get(id=1)
        self.assertEqual(location.name, 'Loc1')

    def test_name_is_not_name(self):
        """
        Test the Brand name blank.
        """
        location = Location.objects.get(id=1)
        self.assertNotEqual(location.name, 'Loc2')

    def test_loc_number_is_loc_number(self):
        """
        Test the Brand name blank.
        """
        location = Location.objects.get(id=1)
        self.assertEqual(location.loc_number, 1)
