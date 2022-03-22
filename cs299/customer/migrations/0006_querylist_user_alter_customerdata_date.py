# Generated by Django 4.0.1 on 2022-03-14 20:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_customerdata_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='querylist',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='customer.customerdata'),
        ),
        migrations.AlterField(
            model_name='customerdata',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 15, 1, 41, 40, 690535)),
        ),
    ]