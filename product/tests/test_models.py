from django.test import TestCase

from product.models import Brand, Category


class BrandModelTest(TestCase):
    """
    Test the Brand model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        for i in range(1, 16):
            Brand.objects.create(name=f"Brand {i}")

    def test_name_label(self):
        """
        Test the Brand name label.
        """
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

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
        self.assertEqual(is_unique, True)

    def test_name_blank(self):
        """
        Test the Brand name blank.
        """
        brand = Brand.objects.get(id=1)
        self.assertTrue(brand.name)


class CategoryModelTest(TestCase):
    """
    Test the Category model.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        """
        for i in range(1, 16):
            Category.objects.create(name=f"Category {i}")

    def test_name_label(self):
        """
        Test the Category name label.
        """
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

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
        self.assertEqual(is_unique, True)

    def test_name_blank(self):
        """
        Test the Category name blank.
        """
        category = Category.objects.get(id=1)
        self.assertTrue(category.name)
