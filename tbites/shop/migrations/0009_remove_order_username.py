# Generated by Django 3.1.3 on 2020-12-07 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_order_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='username',
        ),
    ]