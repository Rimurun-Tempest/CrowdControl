# Generated by Django 4.0.1 on 2022-03-14 20:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0012_alter_shopdata_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopdata',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 15, 1, 41, 40, 802520)),
        ),
    ]
