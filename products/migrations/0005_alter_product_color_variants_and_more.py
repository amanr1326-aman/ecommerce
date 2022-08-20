# Generated by Django 4.0.6 on 2022-08-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_colorvariant_sizevariant_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color_variants',
            field=models.ManyToManyField(blank=True, to='products.colorvariant'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_variants',
            field=models.ManyToManyField(blank=True, to='products.sizevariant'),
        ),
    ]