# Generated by Django 4.0.3 on 2022-03-28 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0005_shopkeeper_shop_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopkeeper',
            name='shop_bio',
            field=models.TextField(default=''),
        ),
    ]