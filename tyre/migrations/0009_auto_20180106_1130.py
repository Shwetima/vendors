# Generated by Django 2.0 on 2018-01-06 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tyre', '0008_auto_20180106_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tyre_reciept_from_vehicle',
            name='Nature',
            field=models.CharField(default='Tyre_Reciept_from_Vehicle', max_length=40),
        ),
    ]
