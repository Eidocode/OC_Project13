from django.db import models


class Brand(models.Model):
    # Brand model
    name = models.CharField(max_length=50)


class Category(models.Model):
    # Category model
    name = models.CharField(max_length=50)


class Model(models.Model):
    # Category model
    pass
