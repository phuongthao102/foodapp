# Generated by Django 5.1.5 on 2025-01-22 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Store',
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=1000000000, max_digits=10)),
                ('food_type', models.CharField(max_length=2000)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.store')),
            ],
        ),
    ]
