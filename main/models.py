from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    barcode = models.ImageField(upload_to='barcodes/', blank=True, null=True)
    batch_no = models.CharField(max_length=100)
    expiry_date = models.DateTimeField(null=True, blank=True)
    lot_no = models.CharField(max_length=100)
    unit_price = models.DecimalField(
        max_digits=15, decimal_places=0, default=0)
    active_ingredient = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100)
    atc_code = models.CharField(max_length=100)
    snowmed_code = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(null=True, blank=True)
    cost = models.DecimalField(
        null=True, blank=True, max_digits=15, decimal_places=0)
    quantity = models.IntegerField(null=False, default=0)
    unit_of_measure = models.CharField(null=False, default=0, max_length=100)
    total_quantity = models.IntegerField(default=0, null=True, blank=True)
    issued_quantity = models.IntegerField(default=0, null=True, blank=True)
    received_quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.product.name


class Sale(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    amount_received = models.IntegerField(default=0, null=True, blank=True)
    issued_to = models.CharField(max_length=50, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.item.name
