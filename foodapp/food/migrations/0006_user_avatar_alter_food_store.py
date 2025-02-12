# Generated by Django 5.1.5 on 2025-01-27 09:40

import cloudinary.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_alter_food_description_alter_lesson_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='food',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='food', to='food.store'),
        ),
    ]
