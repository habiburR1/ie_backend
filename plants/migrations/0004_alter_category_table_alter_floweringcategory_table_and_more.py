# Generated by Django 5.1 on 2024-09-16 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_alter_plant_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='Categories_Plants',
        ),
        migrations.AlterModelTable(
            name='floweringcategory',
            table='FloweringCategories_Plants',
        ),
        migrations.AlterModelTable(
            name='location',
            table='Locations_Plants',
        ),
        migrations.AlterModelTable(
            name='maintenancetype',
            table='MaintenanceTypes_Plants',
        ),
    ]