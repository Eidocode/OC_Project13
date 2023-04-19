from django.contrib.auth.models import User
from selenium.webdriver.common.by import By

from product.models import Category, Brand, CpuBrand, OperatingSystem, Location, \
    Entity, Immo, Device, Product, DeviceUser, Inventory, Cpu


def create_tests_data():
    """
    Create tests data
    """
    Category.objects.create(name='Test_Category')
    Brand.objects.create(name='Test_Brand')
    CpuBrand.objects.create(name='Test_CPU_Brand')
    OperatingSystem.objects.create(name='Test_OS')
    Location.objects.create(
        name='Loc',
        loc_number=1234,
        site=Entity.objects.create(name='Test_Entity')
    )
    Immo.objects.create(
        bc_number='45000000',
        inventory_number='12345',
        location=Location.objects.get(
            name='Loc'
        ),
    )
    for i in range(20):
        Device.objects.create(
            product=Product.objects.create(
                name=f'Test Product {i}',
                category=Category.objects.get(name='Test_Category'),
                brand=Brand.objects.get(name='Test_Brand'),
            ),
            device_user=DeviceUser.objects.create(
                first_name=f'Test FName {i}',
                last_name=f'Test LName {i}',
                uid=f'UID_{i}',
            ),
            inventory=Inventory.objects.create(
                hostname=f'Test Hostname {i}',
                serial=f'Test Serial {i}',
                cpu=Cpu.objects.create(
                    name=f'Test CPU {i}',
                    cpu_brand=CpuBrand.objects.get(name='Test_CPU_Brand'),
                ),
                operating_system=OperatingSystem.objects.get(
                    name='Test_OS'
                ),
            ),
            immo=Immo.objects.get(
                bc_number='45000000',
            )
        )


def create_user_for_test(p_user, p_pwd):
    """
    Create a user for the tests
    """
    user = User.objects.create_user(
        username=p_user,
        password=p_pwd,
        email='test_email@test.com',
        first_name='Test_fname',
        last_name='Test_lname',
        is_active=True
    )
    return user


def log_user_for_functional_tests(p_user, p_pwd, p_driver):
    """
    Log the user
    """
    username_input = p_driver.find_element(By.ID, 'id_username')
    username_input.send_keys(p_user)
    password_input = p_driver.find_element(By.ID, 'id_password')
    password_input.send_keys(p_pwd)
    submit_button = p_driver.find_element(By.ID, 'login_btn')
    submit_button.click()
