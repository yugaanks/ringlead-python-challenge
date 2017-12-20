# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_first_name', models.CharField(max_length=200)),
                ('customer_last_initial', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('product_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='products',
            field=models.ManyToManyField(to='apollo.Product'),
        ),
    ]
