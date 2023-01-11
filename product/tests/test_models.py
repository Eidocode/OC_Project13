from django.test import TestCase

from product.models import Brand, Category, Product, CpuBrand, Cpu, Inventory


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
        self.assertEqual(is_unique, True)

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
