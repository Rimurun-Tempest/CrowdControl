# Generated by Django 4.0.3 on 2022-03-27 09:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_customer', models.BooleanField(default=True)),
                ('prefftime1', models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 27, 9, 32, 51, 545141))),
                ('prefftime2', models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 27, 9, 32, 51, 545158))),
                ('prefftime3', models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 27, 9, 32, 51, 545167))),
                ('bit', models.CharField(max_length=10)),
                ('customer', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
