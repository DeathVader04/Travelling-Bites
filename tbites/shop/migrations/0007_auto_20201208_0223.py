# Generated by Django 3.1.3 on 2020-12-07 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='item',
        ),
    ]