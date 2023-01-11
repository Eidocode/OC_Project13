"""
    This file contains the models used for the PSQL Database
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Adds a unique contraint to the email field in the user table
User._meta.get_field('email')._unique = True


class Brand(models.Model):
    """
    Class used for the brand model
    ----------
    name
        Contains the names of the brands used
    """
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    """
    Class used for the category model
    ----------
    name
        Contains the names of the categories used
    """
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    """
    Class used for the product model
    ----------
    name
        Contains the names of the products used
    brand
        Foreign Key that points to the Brand table
    category
        Foreign Key that points to the Category table
    """
    name = models.CharField(max_length=25, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'[{self.category.name}] {self.brand.name} {self.name}'

    class Meta:
        """ Constraint of unicity on name, brand & category """
        unique_together = ('name', 'brand', 'category')


class CpuBrand(models.Model):
    """
    Class used for the CpuBrand model
    ----------
    name
        Contains the names of the Cpu Brands
    """
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.name}'


class Cpu(models.Model):
    """
    Class used for the Cpu model
    ----------
    brand
        Foreign Key that points to the CpuBrand table
    name
        Contains the names of the Cpu models
    frequency
        Contains the CPU frequency
    nb_core
        Contains the number of physical cores
    smt
        Indicates the presence of simultaneous multithreading technology
    """
    cpu_brand = models.ForeignKey(CpuBrand, on_delete=models.PROTECT)
    name = models.CharField(max_length=20, unique=True)
    frequency = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    nb_cores = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return f'{self.cpu_brand.name} {self.name}@{self.frequency}GHz'


class Inventory(models.Model):
    """
    Class used for the Inventory model
    ----------
    hostname
        Contains the hostname of the device
    serial
        Contains the serial number of the device
    warranty_end
        Indicates the end date of the guarantee
    cpu
        Foreign key that points to the Cpu table
    addr_mac
        Contains the mac address of the device
    storage
        Indicates the size of the storage
    """
    hostname = models.CharField(max_length=20)
    serial = models.CharField(max_length=20, unique=True)
    cpu = models.ForeignKey(Cpu, on_delete=models.PROTECT)
    ram = models.PositiveSmallIntegerField(null=True)
    addr_mac = models.CharField(max_length=12, unique=True, null=True)
    storage = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.hostname} with {self.cpu.name}' \
            f'--> S/N : {self.serial}' \
            f'--> Ram : {self.ram} Go' \
            f'--> Storage : {self.storage} Go'


class Status(models.Model):
    """
    Class used for the Status model
    ----------
    name
        Contains the names of the user status
    """
    name = models.CharField(max_length=20, unique=True)


class Assignment(models.Model):
    """
    Class used for the Assignment model
    ----------
    name
        Contains the names of the user assignment
    """
    name = models.CharField(max_length=15, unique=True)


class DeviceUser(models.Model):
    """
    Class used for the DeviceUser model
    ----------
    first_name
        Contains the first name of the user assigned to the device
    last_name
        Contains the last name of the user assigned to the device
    uid
        Contains the UID of the user assigned to the device
    """
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=70, unique=True, null=True)
    uid = models.CharField(max_length=10, unique=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} with {self.uid}'


class Entity(models.Model):
    """
    Class used for the Site model
    ----------
    name
        Contains the names of the different sites
    """
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f'{self.name}'


class Location(models.Model):
    """
    Class used for the Location model
    ----------
    name
        Contains the names of the different location
    loc_number
        Contains the location number
    site
        Foreign Key that points to the Site table
    """
    name = models.CharField(max_length=6)
    loc_number = models.PositiveIntegerField()
    site = models.ForeignKey(Entity, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.site} : {self.name}'

    class Meta:
        """ Constraint of unicity on the association name & site """
        unique_together = ('name', 'loc_number', 'site')


class Immo(models.Model):
    """
    Class used for the Immo model
    ----------
    bc_number
        Contains the purchase order number
    buy_date
        Contains the date of purchase of the device
    inventory_number
        Contains the inventory number of the device
    location
        Foreign key that points to the Location table
    cost_center
        Contains the name of the cost center
    """
    bc_number = models.CharField(max_length=12, null=True)
    inventory_number = models.IntegerField(unique=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.inventory_number} {self.location}'


class Device(models.Model):
    """
    Class used for the Device model
    ----------
    product
        Foreign key that points to the Product table
    added_date
        Date the device was added to the databases
    inventory
        Foreign key that points to the Inventory table
    device_user
        Foreign key that points to the DeviceUser table
    immo
        Foreign key that points to the Immo table
    """
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    added_date = models.DateTimeField(default=timezone.now())
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True)
    device_user = models.ForeignKey(DeviceUser, on_delete=models.PROTECT)
    immo = models.ForeignKey(Immo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.added_date} {self.product.name}'
