# Generated by Django 3.1.3 on 2020-12-07 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20201208_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]