# Generated by Django 5.0.2 on 2024-02-13 20:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('in_stock', models.IntegerField()),
                ('available_stock', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Inventory.category')),
                ('tags', models.ManyToManyField(related_name='items', to='Inventory.tag')),
            ],
        ),
    ]
