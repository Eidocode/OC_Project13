from django.db import models


class Brand(models.Model):
    # Brand model
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    # Category model
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Model(models.Model):
    # Category model
    name = models.CharField(max_length=50, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.category.name}] {self.brand.name} {self.name}'


class CpuBrand(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Cpu(models.Model):
    # CPU model
    brand = models.ForeignKey(CpuBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    frequency = models.FloatField()
    nb_core = models.IntegerField()
    smt = models.BooleanField()

    def __str__(self):
        return f'{self.brand.name} {self.name}@{self.frequency}'


class Inventory(models.Model):
    # Inventory model
    hostname = models.CharField(max_length=25)
    serial = models.CharField(max_length=50, unique=True)
    warranty_end = models.DateTimeField(null=True)
    cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    ram = models.IntegerField()
    addr_mac = models.CharField(max_length=12, unique=True)
    storage = models.IntegerField()

    def __str__(self):
        return f'{self.hostname} ' \
               f'--> S/N : {self.serial}' \
               f'--> {self.cpu.brand.name} {self.cpu.name}@{self.cpu.frequency}' \
               f'--> Ram : {self.ram} Go' \
               f'--> Storage : {self.storage} Go'

    class Meta:
        # Constraint of unicity on the association hostname & serial
        unique_together = ('hostname', 'serial')


class DeviceUser(models.Model):
    # Device User model
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    uid = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} with {self.uid}'


class Site(models.Model):
    # Site model
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Localisation(models.Model):
    # Localisation model
    name = models.CharField(max_length=25)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.site} : {self.name}'

    class Meta:
        # Constraint of unicity on the association name & site
        unique_together = ('name', 'site')


class Immo(models.Model):
    # Immo model
    bc_number = models.IntegerField(null=True)
    buy_date = models.DateTimeField(null=True)
    inventory_number = models.IntegerField(unique=True)
    localisation = models.ForeignKey(Localisation, on_delete=models.CASCADE)
    cost_center = models.CharField(max_length=25, null=True)

    def __str__(self):
        return f'{self.inventory_number} {self.localisation} {self.cost_center}'


class Device(models.Model):
    # Product model
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    device_user = models.ForeignKey(DeviceUser, on_delete=models.CASCADE)
    immo = models.ForeignKey(Immo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.added_date} {self.model.brand.name} {self.model.name} ' \
               f'--> {self.inventory.hostname} ' \
               f'--> {self.device_user.last_name} {self.device_user.first_name}' \
               f'--> {self.immo.inventory_number} {self.immo.localisation}'
