# Generated by Django 4.2.1 on 2023-06-06 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.ImageField(blank=True, null=True, upload_to='barcodes/'),
        ),
    ]
