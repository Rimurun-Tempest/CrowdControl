# Generated by Django 4.0.3 on 2022-03-27 20:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_delete_customerdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='prefftime1',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 27, 20, 48, 36, 634434)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='prefftime2',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 27, 20, 48, 36, 634449)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='prefftime3',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 27, 20, 48, 36, 634457)),
        ),
    ]
